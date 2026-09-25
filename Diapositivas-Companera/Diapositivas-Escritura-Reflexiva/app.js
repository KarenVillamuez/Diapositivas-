/* ==========================================================================
   VI CONGRESO INTERNACIONAL DE INVESTIGACIÓN INTERDISCIPLINAR
   LHXT26 - CARTAGENA DE INDIAS (28-30 OCT 2026)
   Motor de Navegación de Diapositivas 16:9 y Notas de Orador
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const stage = document.getElementById('slides-stage');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const totalSlides = slides.length;
  const progressFill = document.getElementById('progress-fill');
  const notesPanel = document.getElementById('speaker-notes-panel');
  const notesContent = document.getElementById('speaker-notes-content');
  const notesIndicator = document.getElementById('notes-slide-indicator');
  
  let currentSlideIndex = 0;
  let showNotes = false;

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
  // 2. ACTUALIZACIÓN DE NOTAS DEL ORADOR
  // ========================================================================
  function updateNotes() {
    if (!notesPanel || !notesContent) return;
    const activeSlide = slides[currentSlideIndex];
    if (!activeSlide) return;

    const notesText = activeSlide.getAttribute('data-notes') || 'Sin notas específicas para esta diapositiva.';
    notesContent.innerHTML = notesText;
    if (notesIndicator) {
      notesIndicator.textContent = `Diapositiva ${currentSlideIndex + 1} de ${totalSlides}`;
    }

    notesPanel.style.display = showNotes ? 'block' : 'none';
  }

  // ========================================================================
  // 3. NAVEGACIÓN ENTRE DIAPOSITIVAS
  // ========================================================================
  function goToSlide(index, updateHash = true) {
    if (index < 0 || index >= totalSlides) return;

    slides.forEach((s, idx) => {
      s.classList.toggle('active', idx === index);
    });

    currentSlideIndex = index;

    // Actualizar barra de progreso
    if (progressFill && totalSlides > 1) {
      const pct = (currentSlideIndex / (totalSlides - 1)) * 100;
      progressFill.style.width = `${pct}%`;
    }

    // Actualizar notas
    updateNotes();

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

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    }
  }

  // ========================================================================
  // 4. CONTROL POR TECLADO
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

      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      case 'n':
      case 'N':
        e.preventDefault();
        showNotes = !showNotes;
        updateNotes();
        break;
    }
  });

  // ========================================================================
  // 5. SINCRONIZACIÓN CON URL HASH (#slide-1, #slide-2...)
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
