document.addEventListener('contextmenu', event => {
  event.preventDefault();
});

document.addEventListener("DOMContentLoaded", () => {
    // ================================
    // Section Visibility & Dot Navigation
    // ================================

    const sections = document.querySelectorAll(".snap-section");
    const dots = document.querySelectorAll(".timeline-nav .dot");

    // Highlight active timeline dot based on scroll position
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const index = Array.from(sections).indexOf(entry.target);
            if (entry.isIntersecting) {
                dots.forEach(dot => dot.classList.remove("active"));
                if (dots[index]) dots[index].classList.add("active");
            }
        });
    }, {
        threshold: 0.6
    });

    sections.forEach(section => observer.observe(section));

    // Reveal section content with fade-in animation
    const lazyObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const content = entry.target.querySelector(".section-content");
                if (content && !content.classList.contains("visible")) {
                    content.classList.remove("hidden");
                    content.classList.add("visible");
                }
            }
        });
    }, {
        threshold: 0.4
    });

    sections.forEach(section => lazyObserver.observe(section));

    // ================================
    // Theme Switcher Logic
    // ================================

    const themeButton = document.getElementById('themeButton');
    const themes = ['light', 'dark', 'colorful'];
    let currentTheme = localStorage.getItem('theme') || 'light';

    /**
     * Updates the body theme attribute and persists the setting.
     */
    function updateTheme(theme) {
        document.body.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }

    updateTheme(currentTheme);

    if (themeButton) {
        themeButton.addEventListener('click', () => {
            const nextIndex = (themes.indexOf(currentTheme) + 1) % themes.length;
            currentTheme = themes[nextIndex];
            updateTheme(currentTheme);
        });
    }

    // ================================
    // Imprint Modal (open/close)
    // ================================

    const imprintBtn = document.getElementById("imprintButton");
    const imprintModal = document.getElementById("imprintModal");
    const imprintClose = document.getElementById("imprintClose");

    if (imprintBtn && imprintModal && imprintClose) {
        imprintBtn.addEventListener("click", () => {
            imprintModal.style.display = "block";
        });

        imprintClose.addEventListener("click", () => {
            imprintModal.style.display = "none";
        });

        window.addEventListener("click", (event) => {
            if (event.target === imprintModal) {
                imprintModal.style.display = "none";
            }
        });
    }
});

// ================================
// Touch-Swipe Support for Project Slider
// ================================

// Store the horizontal start and end position of touch events
let startX = 0;
let endX = 0;

// Reference to the slider track container holding project slides
const sliderTrack = document.getElementById('projectTrack');

if (sliderTrack) {
    // Capture the X position when touch starts
    sliderTrack.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
    });

    // Capture the X position when touch ends and handle swipe
    sliderTrack.addEventListener('touchend', (e) => {
        endX = e.changedTouches[0].clientX;
        handleSwipe();
    });
}

/**
 * Handles swipe detection and triggers slide navigation.
 * Only triggers if swipe distance exceeds a threshold.
 */
function handleSwipe() {
    const threshold = 50;  // Minimum swipe distance in pixels to trigger slide
    const deltaX = endX - startX;

    if (Math.abs(deltaX) > threshold) {
        // Swipe left -> next slide, swipe right -> previous slide
        slideProjects(deltaX < 0 ? 1 : -1);
    }
}

// ================================
// Mobile Menu Toggle Logic
// ================================

const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');

if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('show');
        menuToggle.classList.toggle('open');
    });
}

/**
 * Closes the mobile menu with a short delay.
 */
window.closeMenu = function () {
    setTimeout(() => {
        mobileMenu.classList.remove('show');
        menuToggle.classList.remove('open');
    }, 50);
};

// ================================
// Mobile Menu Link Scroll Behavior
// ================================

function handleMenuClick(event, targetId) {
    event.preventDefault();

    const target = document.getElementById(targetId);
    if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
    }

    closeMenu();
    history.replaceState(null, '', ' ');
}

// ================================
// Timeline Dot Scroll Navigation
// ================================

document.querySelectorAll('.timeline-nav .dot').forEach(dot => {
    dot.addEventListener('click', event => {
        event.preventDefault();
        const targetId = dot.getAttribute('data-target');
        const target = document.getElementById(targetId);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
            history.replaceState(null, '', ' ');
        }
    });
});
