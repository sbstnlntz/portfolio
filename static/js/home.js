let projectController = null;
let sliderStarted = false;

/**
 * Creates an infinite-loop horizontal slider controller.
 *
 * @param {string} trackId - ID of the slider track element.
 * @param {number} autoInterval - Milliseconds between automatic slides.
 * @returns {object|null} A controller with `slide()` and `destroy()` methods, or null if not initialized.
 */
function createSliderController(trackId, autoInterval = 7000) {
    const track = document.getElementById(trackId);
    if (!track) return null;

    const state = {
        index: 1, // Start at first real slide (after the prepended clone)
        isTransitioning: false,
        intervalId: null,
        slideWidth: track.querySelector(".slide")?.offsetWidth || track.parentElement.offsetWidth,
    };

    /**
     * Slides to the next or previous item.
     * @param {number} direction - 1 for next, -1 for previous
     */
    const slide = (direction = 1) => {
        if (state.isTransitioning) return;

        const slides = track.children;
        const total = slides.length;
        state.index += direction;
        state.isTransitioning = true;

        track.style.transition = "transform 0.4s ease-in-out";
        track.style.transform = `translateX(-${state.index * state.slideWidth}px)`;

        setTimeout(() => {
            if (state.index === total - 1) {
                // Jump back to real first slide
                track.style.transition = "none";
                state.index = 1;
                track.style.transform = `translateX(-${state.index * state.slideWidth}px)`;
            }
            if (state.index === 0) {
                // Jump to real last slide
                track.style.transition = "none";
                state.index = total - 2;
                track.style.transform = `translateX(-${state.index * state.slideWidth}px)`;
            }
            state.isTransitioning = false;
        }, 400);
    };

    /**
     * Initializes the slider and starts automatic sliding.
     */
    const init = () => {
        track.style.transition = "none";
        track.style.transform = `translateX(-${state.slideWidth}px)`;
        state.intervalId = setInterval(() => slide(1), autoInterval);
    };

    init();

    return {
        slide,
        destroy: () => clearInterval(state.intervalId),
        updateWidth: () => {
            state.slideWidth = track.querySelector(".slide")?.offsetWidth || track.parentElement.offsetWidth;
            track.style.transition = "none";
            track.style.transform = `translateX(-${state.index * state.slideWidth}px)`;
        },
    };
}

/**
 * Loops through skill icons using a fade-in/out effect.
 *
 * @param {number} interval - Time between icon transitions (ms)
 */
function cycleSkillIcons(interval = 3000) {
    const images = document.querySelectorAll('.skills-image-wrapper .skills-image');
    if (images.length === 0) return;

    let current = 0;
    setInterval(() => {
        images[current].classList.remove('visible');
        current = (current + 1) % images.length;
        images[current].classList.add('visible');
    }, interval);
}

/**
 * Slides the project carousel left/right.
 *
 * @param {number} direction - Use 1 for next, -1 for previous
 */
function slideProjects(direction) {
    if (projectController) {
        projectController.slide(direction);
    }
}

/**
 * Observes the #projects section and triggers slider init when visible.
 */
function observeProjectsSection() {
    const section = document.getElementById('projects');
    if (!section) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !sliderStarted) {
                projectController = createSliderController("projectTrack", 7000);
                sliderStarted = true;
                observer.disconnect(); // No longer needed
            }
        });
    }, {
        threshold: 0.4
    });

    observer.observe(section);
}

/**
 * Updates the slider width and position on window resize.
 */
window.addEventListener("resize", () => {
    if (projectController) {
        projectController.updateWidth();
    }
});

/**
 * Stops the slider when the tab is hidden, restarts it when visible.
 */
document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
        projectController?.destroy();
    } else if (sliderStarted) {
        projectController = createSliderController("projectTrack", 7000);
    }
});

/**
 * Initialize slider and skill icons on full page load.
 */
window.addEventListener("load", () => {
    observeProjectsSection();   // Lazy-init the slider when in view
    cycleSkillIcons(2500);      // Start skill icon rotation
});
