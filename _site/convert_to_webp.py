#!/usr/bin/env python3
"""
Convert PNG/JPEG images to WebP format for better compression.
"""

import os
from pathlib import Path
from PIL import Image
import argparse


def get_file_size_mb(filepath):
    """Get file size in MB."""
    return os.path.getsize(filepath) / (1024 * 1024)


def convert_to_webp(filepath, quality=80, dry_run=False):
    """
    Convert an image to WebP format.

    Args:
        filepath: Path to the image file
        quality: WebP quality (1-100)
        dry_run: If True, only show what would be done

    Returns:
        Tuple of (original_size_mb, new_size_mb, savings_percent)
    """
    original_size = get_file_size_mb(filepath)
    webp_path = filepath.with_suffix('.webp')

    # Skip if already WebP
    if filepath.suffix.lower() == '.webp':
        print(f"  ⏭️  Already WebP format")
        return original_size, original_size, 0

    try:
        img = Image.open(filepath)

        if dry_run:
            print(f"  [DRY RUN] Would convert to {webp_path.name}")
            return original_size, original_size, 0

        # Save as WebP
        img.save(webp_path, 'WEBP', quality=quality, method=6)
        new_size = get_file_size_mb(webp_path)

        # Only replace if WebP is smaller
        if new_size < original_size:
            os.remove(filepath)
            savings = ((original_size - new_size) / original_size * 100)
            print(f"  ✅ Converted to WebP: {filepath.suffix} → .webp")
            return original_size, new_size, savings
        else:
            os.remove(webp_path)
            print(f"  ⏭️  WebP not smaller, keeping original")
            return original_size, original_size, 0

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return original_size, original_size, 0


def convert_directory(directory, quality=80, dry_run=False, extensions=None):
    """Convert all images in directory to WebP."""
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png']

    directory = Path(directory)

    # Find all image files
    image_files = []
    for ext in extensions:
        image_files.extend(directory.rglob(f"*{ext}"))
        image_files.extend(directory.rglob(f"*{ext.upper()}"))

    if not image_files:
        print(f"No image files found in {directory}")
        return

    print(f"\n{'=' * 70}")
    print(f"🔄 Converting to WebP {'[DRY RUN]' if dry_run else ''}")
    print(f"{'=' * 70}")
    print(f"Directory: {directory}")
    print(f"Quality: {quality}")
    print(f"Found {len(image_files)} image(s)\n")

    total_original = 0
    total_new = 0
    converted = 0

    for filepath in sorted(image_files):
        print(f"\n📁 {filepath.relative_to(directory)}")
        original, new, savings = convert_to_webp(filepath, quality, dry_run)

        total_original += original
        total_new += new

        if savings > 0:
            converted += 1
            print(f"  💾 {original:.2f} MB → {new:.2f} MB ({savings:+.1f}%)")

    # Summary
    print(f"\n{'=' * 70}")
    print(f"📊 Summary")
    print(f"{'=' * 70}")
    print(f"Converted: {converted} file(s)")
    print(f"Total original size: {total_original:.2f} MB")
    print(f"Total new size: {total_new:.2f} MB")
    total_savings = ((total_original - total_new) / total_original * 100) if total_original > 0 else 0
    print(f"Total savings: {total_original - total_new:.2f} MB ({total_savings:.1f}%)")
    print(f"{'=' * 70}\n")


def main():
    parser = argparse.ArgumentParser(description='Convert images to WebP format')
    parser.add_argument('--dir', default='assets/images', help='Directory to process')
    parser.add_argument('--quality', type=int, default=80, help='WebP quality (1-100)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without modifying')

    args = parser.parse_args()
    convert_directory(args.dir, quality=args.quality, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
