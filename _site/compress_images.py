#!/usr/bin/env python3
"""
Image compression script for Jekyll blog assets.
Compresses images in-place to reduce file sizes and improve loading times.
"""

import os
import sys
from pathlib import Path
from PIL import Image
import argparse


def get_file_size_mb(filepath):
    """Get file size in MB."""
    return os.path.getsize(filepath) / (1024 * 1024)


def compress_image(filepath, quality=85, max_width=1920, dry_run=False):
    """
    Compress an image file in-place.

    Args:
        filepath: Path to the image file
        quality: JPEG quality (1-100), or PNG compression level mapping
        max_width: Maximum width to resize to (maintains aspect ratio)
        dry_run: If True, only show what would be done without modifying files

    Returns:
        Tuple of (original_size_mb, new_size_mb, savings_percent)
    """
    original_size = get_file_size_mb(filepath)

    try:
        # Open image
        img = Image.open(filepath)

        # Convert RGBA to RGB for JPEG
        if filepath.suffix.lower() in ['.jpg', '.jpeg'] and img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background

        # Resize if image is too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            print(f"  📐 Resized to {max_width}x{new_height}")

        if dry_run:
            print(f"  [DRY RUN] Would compress {filepath.name}")
            return original_size, original_size, 0

        # Save with compression
        if filepath.suffix.lower() in ['.jpg', '.jpeg']:
            img.save(filepath, 'JPEG', quality=quality, optimize=True, progressive=True)
        elif filepath.suffix.lower() == '.png':
            # PNG quality mapping: 85 -> compress_level 6
            compress_level = max(1, min(9, int((100 - quality) / 10)))
            img.save(filepath, 'PNG', optimize=True, compress_level=compress_level)
        elif filepath.suffix.lower() == '.gif':
            img.save(filepath, 'GIF', optimize=True)
        elif filepath.suffix.lower() == '.webp':
            img.save(filepath, 'WEBP', quality=quality, method=6)
        else:
            print(f"  ⏭️  Skipping unsupported format: {filepath.suffix}")
            return original_size, original_size, 0

        new_size = get_file_size_mb(filepath)
        savings = ((original_size - new_size) / original_size * 100) if original_size > 0 else 0

        return original_size, new_size, savings

    except Exception as e:
        print(f"  ❌ Error processing {filepath}: {e}")
        return original_size, original_size, 0


def compress_directory(directory, quality=85, max_width=1920, dry_run=False, extensions=None):
    """
    Compress all images in a directory recursively.

    Args:
        directory: Path to directory containing images
        quality: Compression quality (1-100)
        max_width: Maximum width for images
        dry_run: If True, only show what would be done
        extensions: List of file extensions to process (default: common image formats)
    """
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

    directory = Path(directory)
    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        return

    # Find all image files
    image_files = []
    for ext in extensions:
        image_files.extend(directory.rglob(f"*{ext}"))
        image_files.extend(directory.rglob(f"*{ext.upper()}"))

    if not image_files:
        print(f"No image files found in {directory}")
        return

    print(f"\n{'=' * 70}")
    print(f"🖼️  Image Compression {'[DRY RUN]' if dry_run else ''}")
    print(f"{'=' * 70}")
    print(f"Directory: {directory}")
    print(f"Quality: {quality}")
    print(f"Max width: {max_width}px")
    print(f"Found {len(image_files)} image(s)\n")

    total_original = 0
    total_new = 0
    processed = 0

    for filepath in sorted(image_files):
        print(f"\n📁 {filepath.relative_to(directory)}")
        original, new, savings = compress_image(filepath, quality, max_width, dry_run)

        if original > 0:
            total_original += original
            total_new += new
            processed += 1

            print(f"  💾 {original:.2f} MB → {new:.2f} MB ({savings:+.1f}%)")

    # Summary
    print(f"\n{'=' * 70}")
    print(f"📊 Summary")
    print(f"{'=' * 70}")
    print(f"Processed: {processed} file(s)")
    print(f"Total original size: {total_original:.2f} MB")
    print(f"Total new size: {total_new:.2f} MB")
    total_savings = ((total_original - total_new) / total_original * 100) if total_original > 0 else 0
    print(f"Total savings: {total_original - total_new:.2f} MB ({total_savings:.1f}%)")
    print(f"{'=' * 70}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Compress images in Jekyll blog assets',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compress_images.py                    # Compress all images in assets/images/
  python compress_images.py --dry-run          # Preview what would be compressed
  python compress_images.py --quality 90       # Higher quality (less compression)
  python compress_images.py --max-width 1200   # Resize large images to 1200px width
  python compress_images.py --dir assets/      # Compress all images in assets/
        """
    )

    parser.add_argument(
        '--dir',
        default='assets/images',
        help='Directory to compress images in (default: assets/images)'
    )
    parser.add_argument(
        '--quality',
        type=int,
        default=85,
        help='Compression quality 1-100 (default: 85)'
    )
    parser.add_argument(
        '--max-width',
        type=int,
        default=1920,
        help='Maximum width for images in pixels (default: 1920)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without modifying files'
    )

    args = parser.parse_args()

    # Validate quality
    if not 1 <= args.quality <= 100:
        print("❌ Quality must be between 1 and 100")
        sys.exit(1)

    compress_directory(
        args.dir,
        quality=args.quality,
        max_width=args.max_width,
        dry_run=args.dry_run
    )


if __name__ == '__main__':
    main()
