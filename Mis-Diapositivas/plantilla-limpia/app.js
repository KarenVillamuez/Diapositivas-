/* ==========================================================================
   VI CONGRESO INTERNACIONAL DE INVESTIGACIÓN INTERDISCIPLINAR
   LHXT26 - CARTAGENA DE INDIAS (28-30 OCT 2026)
   Motor de Navegación y Herramientas del Ponente (Plantilla Base)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const stage = document.getElementById('slides-stage');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const totalSlides = slides.length;
  let currentSlideIndex = 0;

  // Elementos de la interfaz
  const progressFill = document.getElementById('progress-fill');
  const slideCounter = document.getElementById('slide-counter');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnFullscreen = document.getElementById('btn-fullscreen');
  const btnOverview = document.getElementById('btn-overview');
  const btnCloseOverview = document.getElementById('btn-close-overview');
  const overviewModal = document.getElementById('overview-modal');
  const overviewGrid = document.getElementById('overview-grid');
  const btnLaser = document.getElementById('btn-laser');
  const laserPointer = document.getElementById('laser-pointer');
  const btnPdf = document.getElementById('btn-pdf');
  const timerDisplay = document.getElementById('timer-display');
  const speakerTimer = document.getElementById('speaker-timer');
  const presenterToolbar = document.getElementById('presenter-toolbar');

  // Auto-activación de toolbar al mover el mouse
  let mouseMoveTimeout = null;
  window.addEventListener('mousemove', () => {
    presenterToolbar.classList.add('active-hover');
    clearTimeout(mouseMoveTimeout);
    mouseMoveTimeout = setTimeout(() => {
      presenterToolbar.classList.remove('active-hover');
    }, 2800);
  });

  // ========================================================================
  // 1. ESCALADO AUTOMÁTICO 16:9 EN CUALQUIER PANTALLA
  // ========================================================================
  const BASE_WIDTH = 1920;
  const BASE_HEIGHT = 1080;

  function resizeStage() {
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

    slides[currentSlideIndex].classList.remove('active');
    currentSlideIndex = index;
    slides[currentSlideIndex].classList.add('active');

    // Actualizar Contador
    const numStr = String(currentSlideIndex + 1).padStart(2, '0');
    const totStr = String(totalSlides).padStart(2, '0');
    slideCounter.textContent = `${numStr} / ${totStr}`;

    // Actualizar Barra de Progreso
    const progressPercent = ((currentSlideIndex + 1) / totalSlides) * 100;
    progressFill.style.width = `${progressPercent}%`;

    // Actualizar Hash en la URL
    if (updateHash) {
      window.location.hash = `slide-${currentSlideIndex + 1}`;
    }

    // Actualizar selección en el overview si está abierto
    updateOverviewActive();
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

  btnPrev.addEventListener('click', prevSlide);
  btnNext.addEventListener('click', nextSlide);

  // ========================================================================
  // 3. ATAJOS DE TECLADO
  // ========================================================================
  window.addEventListener('keydown', (e) => {
    // Si el modal de overview está abierto
    if (overviewModal.classList.contains('open')) {
      if (e.key === 'Escape') {
        toggleOverview(false);
      }
      return;
    }

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

      case 'h':
      case 'H':
        presenterToolbar.classList.toggle('hidden');
        break;

      case 'f':
      case 'F':
        toggleFullscreen();
        break;

      case 'o':
      case 'O':
        toggleOverview(true);
        break;

      case 'l':
      case 'L':
        toggleLaser();
        break;

      case 't':
      case 'T':
        toggleTimer();
        break;
    }
  });

  // ========================================================================
  // 4. MODO PANTALLA COMPLETA
  // ========================================================================
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  btnFullscreen.addEventListener('click', toggleFullscreen);

  // ========================================================================
  // 5. CRONÓMETRO DE ORADOR (15 MINUTOS PARA EL CONGRESO)
  // ========================================================================
  let timerSeconds = 15 * 60; // 15 minutos estándar de ponencia
  let timerRunning = true;
  let timerInterval = null;

  function updateTimerDisplay() {
    const mins = Math.floor(timerSeconds / 60);
    const secs = timerSeconds % 60;
    timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    if (timerSeconds <= 60) {
      speakerTimer.className = 'speaker-timer danger';
    } else if (timerSeconds <= 180) {
      speakerTimer.className = 'speaker-timer warning';
    } else {
      speakerTimer.className = 'speaker-timer';
    }
  }

  function startTimer() {
    timerInterval = setInterval(() => {
      if (timerRunning && timerSeconds > 0) {
        timerSeconds--;
        updateTimerDisplay();
      }
    }, 1000);
  }

  function toggleTimer() {
    timerRunning = !timerRunning;
    speakerTimer.style.opacity = timerRunning ? '1' : '0.6';
  }

  speakerTimer.addEventListener('click', toggleTimer);
  speakerTimer.addEventListener('dblclick', (e) => {
    e.stopPropagation();
    timerSeconds = 15 * 60;
    timerRunning = true;
    speakerTimer.style.opacity = '1';
    updateTimerDisplay();
  });

  startTimer();

  // ========================================================================
  // 6. PUNTERO LÁSER VIRTUAL (TECLA L O BOTÓN)
  // ========================================================================
  let laserActive = false;

  function toggleLaser() {
    laserActive = !laserActive;
    laserPointer.style.display = laserActive ? 'block' : 'none';
    btnLaser.classList.toggle('active', laserActive);
    document.body.style.cursor = laserActive ? 'none' : 'default';
  }

  btnLaser.addEventListener('click', toggleLaser);

  window.addEventListener('mousemove', (e) => {
    if (laserActive) {
      laserPointer.style.left = `${e.clientX}px`;
      laserPointer.style.top = `${e.clientY}px`;
    }
  });

  // ========================================================================
  // 7. VISTA RESUMEN / GRILLA DE DIAPOSITIVAS (OVERVIEW)
  // ========================================================================
  function buildOverviewGrid() {
    overviewGrid.innerHTML = '';
    slides.forEach((slide, idx) => {
      const isDark = slide.classList.contains('s-cover');
      let title = `Diapositiva ${idx + 1}`;
      
      const categoryEl = slide.querySelector('.sh-category');
      const titleEl = slide.querySelector('.s-page-title') || slide.querySelector('.s1-main-title') || slide.querySelector('.s4-title') || slide.querySelector('.s11-main-title');
      
      if (titleEl) {
        title = titleEl.textContent.trim();
      } else if (categoryEl) {
        title = categoryEl.textContent.trim();
      }

      const card = document.createElement('div');
      card.className = `overview-thumb ${isDark ? 'dark' : ''} ${idx === currentSlideIndex ? 'active' : ''}`;
      card.innerHTML = `
        <div class="thumb-num">#${String(idx + 1).padStart(2, '0')}</div>
        <div class="thumb-title">${title}</div>
      `;

      card.addEventListener('click', () => {
        goToSlide(idx);
        toggleOverview(false);
      });

      overviewGrid.appendChild(card);
    });
  }

  function updateOverviewActive() {
    const thumbs = overviewGrid.querySelectorAll('.overview-thumb');
    thumbs.forEach((thumb, idx) => {
      thumb.classList.toggle('active', idx === currentSlideIndex);
    });
  }

  function toggleOverview(open) {
    if (open) {
      buildOverviewGrid();
      overviewModal.classList.add('open');
    } else {
      overviewModal.classList.remove('open');
    }
  }

  btnOverview.addEventListener('click', () => toggleOverview(true));
  slideCounter.addEventListener('click', () => toggleOverview(true));
  btnCloseOverview.addEventListener('click', () => toggleOverview(false));

  // ========================================================================
  // 8. EXPORTACIÓN A PDF (Ctrl + P)
  // ========================================================================
  btnPdf.addEventListener('click', () => {
    window.print();
  });

  // ========================================================================
  // 9. DETECCIÓN DE HASH INICIAL EN URL (#slide-3)
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
