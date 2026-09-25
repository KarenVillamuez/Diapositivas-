/* ==========================================================================
   VI CONGRESO INTERNACIONAL DE INVESTIGACIÓN INTERDISCIPLINAR
   LHXT26 - CARTAGENA DE INDIAS (28-30 OCT 2026)
   Motor de Navegación Simple por Teclas de Flecha
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const stage = document.getElementById('slides-stage');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const totalSlides = slides.length;
  let currentSlideIndex = 0;

  // ========================================================================
  // 1. ESCALADO AUTOMÁTICO 16:9 EN CUALQUIER RESOLUCIÓN
  // ========================================================================
  const BASE_WIDTH = 1920;
  const BASE_HEIGHT = 1080;

  function resizeStage() {
    if (!stage) return;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    const scaleX = windowWidth / BASE_WIDTH;
    const scaleY = windowHeight / BASE_HEIGHT;
    const scale = Math.min(scaleX, scaleY);

    stage.style.setProperty('--canvas-scale', scale);
    stage.style.transform = `scale(${scale})`;
  }

  window.addEventListener('resize', resizeStage);
  resizeStage();

  // ========================================================================
  // 2. NAVEGACIÓN ENTRE DIAPOSITIVAS
  // ========================================================================
  function goToSlide(index, updateHash = true) {
    if (index < 0 || index >= totalSlides) return;

    slides.forEach((s, idx) => {
      s.classList.toggle('active', idx === index);
    });

    currentSlideIndex = index;

    if (updateHash) {
      window.location.hash = `slide-${currentSlideIndex + 1}`;
    }
  }

  function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
      goToSlide(currentSlideIndex + 1);
    }
  }

  function prevSlide() {
    if (currentSlideIndex > 0) {
      goToSlide(currentSlideIndex - 1);
    }
  }

  // ========================================================================
  // 3. NAVEGACIÓN POR TECLADO (FLECHAS, ESPACIO, ETC.)
  // ========================================================================
  window.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case ' ':
      case 'PageDown':
        e.preventDefault();
        nextSlide();
        break;

      case 'ArrowLeft':
      case 'ArrowUp':
      case 'Backspace':
      case 'PageUp':
        e.preventDefault();
        prevSlide();
        break;

      case 'Home':
        e.preventDefault();
        goToSlide(0);
        break;

      case 'End':
        e.preventDefault();
        goToSlide(totalSlides - 1);
        break;
    }
  });

  // ========================================================================
  // 4. SINCRONIZACIÓN CON URL (#slide-1, #slide-2...)
  // ========================================================================
  function handleInitialHash() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#slide-')) {
      const slideNum = parseInt(hash.replace('#slide-', ''), 10);
      if (!isNaN(slideNum) && slideNum >= 1 && slideNum <= totalSlides) {
        goToSlide(slideNum - 1, false);
        return;
      }
    }
    goToSlide(0, false);
  }

  window.addEventListener('hashchange', handleInitialHash);
  handleInitialHash();
});
