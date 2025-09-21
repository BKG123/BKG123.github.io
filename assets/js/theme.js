// Theme switching functionality
(function() {
  'use strict';

  const THEME_KEY = 'site-theme';
  const DARK_THEME = 'dark';
  const LIGHT_THEME = 'light';

  // Get saved theme or default to dark
  function getSavedTheme() {
    try {
      return localStorage.getItem(THEME_KEY) || DARK_THEME;
    } catch (error) {
      console.warn('localStorage not available, using default theme');
      return DARK_THEME;
    }
  }

  // Save theme preference
  function saveTheme(theme) {
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch (error) {
      console.warn('Could not save theme preference');
    }
  }

  // Apply theme to document
  function applyTheme(theme) {
    const root = document.documentElement;

    if (theme === LIGHT_THEME) {
      root.setAttribute('data-theme', 'light');
    } else {
      root.removeAttribute('data-theme');
    }

    // Update theme icon
    updateThemeIcon(theme);
  }

  // Update the theme toggle icon
  function updateThemeIcon(theme) {
    const themeIcon = document.querySelector('.theme-icon');
    if (themeIcon) {
      themeIcon.textContent = theme === LIGHT_THEME ? '🌙' : '☀️';
      themeIcon.setAttribute('aria-label',
        `Switch to ${theme === LIGHT_THEME ? 'dark' : 'light'} theme`
      );
    }
  }

  // Toggle between themes
  function toggleTheme() {
    const currentTheme = getSavedTheme();
    const newTheme = currentTheme === LIGHT_THEME ? DARK_THEME : LIGHT_THEME;

    saveTheme(newTheme);
    applyTheme(newTheme);
  }

  // Initialize theme on page load
  function initTheme() {
    const savedTheme = getSavedTheme();
    applyTheme(savedTheme);

    // Add click listener to theme toggle
    const themeToggle = document.querySelector('.theme-icon');
    if (themeToggle) {
      themeToggle.addEventListener('click', toggleTheme);
      themeToggle.style.cursor = 'pointer';
      themeToggle.setAttribute('role', 'button');
      themeToggle.setAttribute('tabindex', '0');

      // Add keyboard support
      themeToggle.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggleTheme();
        }
      });
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }

  // Expose theme functions globally if needed
  window.siteTheme = {
    toggle: toggleTheme,
    get: getSavedTheme,
    set: function(theme) {
      saveTheme(theme);
      applyTheme(theme);
    }
  };
})();