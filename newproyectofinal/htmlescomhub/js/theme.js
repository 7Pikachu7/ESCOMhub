// js/theme.js
document.addEventListener('DOMContentLoaded', () => {
    const themeToggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

    function applyTheme(theme) {
        if (theme === 'dark') {
            document.body.classList.add('dark-mode');
            themeToggleButton.textContent = '☀️'; // Icono para cambiar a modo claro
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.remove('dark-mode');
            themeToggleButton.textContent = '🌙'; // Icono para cambiar a modo oscuro
            localStorage.setItem('theme', 'light');
        }
    }

    // Aplicar tema guardado o preferencia del sistema
    if (currentTheme) {
        applyTheme(currentTheme);
    } else if (prefersDarkScheme.matches) {
        applyTheme('dark');
    } else {
        applyTheme('light'); // Por defecto a claro si no hay nada guardado ni preferencia del sistema
    }

    // Listener para el botón
    themeToggleButton.addEventListener('click', () => {
        let theme = localStorage.getItem('theme');
        if (theme === 'dark') {
            applyTheme('light');
        } else {
            applyTheme('dark');
        }
    });

    // Listener para cambios en la preferencia del sistema (opcional, pero bueno para UX)
    prefersDarkScheme.addEventListener('change', (e) => {
        // Solo cambia si el usuario no ha establecido una preferencia manualmente
        if (!localStorage.getItem('theme-manual-override')) {
             applyTheme(e.matches ? 'dark' : 'light');
        }
    });

    // Marcar que el usuario ha interactuado si hace clic en el botón
    themeToggleButton.addEventListener('click', () => {
        localStorage.setItem('theme-manual-override', 'true');
    });

});
