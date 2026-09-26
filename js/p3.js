/**
 * ==========================================================================
 * P2 - MOTION E INTERAÇÕES (PERFORMANCE-FIRST)
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Reveal (Fade Up) Observer
  const fadeElements = document.querySelectorAll('.fade-up');

  const fadeObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target); // Para de observar após animar
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -10% 0px',
    threshold: 0.1
  });

  fadeElements.forEach(el => fadeObserver.observe(el));

  // 2. FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');

    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Fecha todos no mobile (opcional, mas recomendado nas regras do usuário)
      faqItems.forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-a').style.maxHeight = null;
      });

      // Se não estava aberto, abre este
      if (!isOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + "px";
      }
    });
  });

  // 3. Floating CTA Logic (Aparece apenas quando não há botões na tela, após a primeira dobra)
  const floatingCta = document.getElementById('floatingCta');
  const headerSection = document.querySelector('header');
  const allOtherBtns = document.querySelectorAll('.btn:not(#floatingCta .btn)');

  let isPastHeader = false;
  let visibleBtns = 0;

  function updateFloatingCta() {
    if (floatingCta) {
      if (isPastHeader && visibleBtns === 0) {
        floatingCta.classList.add('visible');
      } else {
        floatingCta.classList.remove('visible');
      }
    }
  }

  if (floatingCta && headerSection) {
    const headerObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        isPastHeader = !entry.isIntersecting && entry.boundingClientRect.bottom < 0;
        updateFloatingCta();
      });
    }, { root: null, threshold: 0 });
    headerObserver.observe(headerSection);
  }

  if (floatingCta && allOtherBtns.length > 0) {
    const btnObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          visibleBtns++;
        } else {
          visibleBtns--;
        }
      });
      if (visibleBtns < 0) visibleBtns = 0;
      updateFloatingCta();
    }, { root: null, threshold: 0 });
    
    allOtherBtns.forEach(btn => btnObserver.observe(btn));
  }
  // 4. Cycle Infographic Animation (Auto-play without sticky)
  const cycleInfographic = document.querySelector('.cycle-infographic');

  if (cycleInfographic) {
    const steps = cycleInfographic.querySelectorAll('.cycle-step');

    const cycleObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Quando o infográfico entra na tela, iniciamos a montagem do ciclo
          steps.forEach((step, index) => {
            if (window.innerWidth > 900) {
              // No Desktop, aparece rápido pois já está visível
              setTimeout(() => {
                step.classList.add('visible');
              }, index * 100);
            } else {
              // No Mobile, constrói sequencialmente e com charme
              setTimeout(() => {
                step.classList.add('visible');
              }, 300 + (index * 350));
            }
          });
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.15 // Dispara quando 15% estiver visível
    });

    cycleObserver.observe(cycleInfographic);
  }
});

// ==========================================
// BARRA DE PROGRESSO DO LOTE
// ==========================================
let progressAnimated = false;

function animateProgressBar(targetPercentage) {
  if (progressAnimated) return;
  progressAnimated = true;

  const fill = document.getElementById('lote-progress');
  const text = document.getElementById('lote-text');
  const fillFloat = document.getElementById('lote-progress-float');
  const textFloat = document.getElementById('lote-text-float');
  const fillOffer = document.getElementById('lote-progress-offer');
  const textOffer = document.getElementById('lote-text-offer');

  if (fill && text) {
    const widthStr = targetPercentage.toFixed(1) + '%';
    fill.style.width = widthStr;
    if (fillFloat) fillFloat.style.width = widthStr;
    if (fillOffer) fillOffer.style.width = widthStr;
    
    let currentNumber = 0;
    const targetNumber = parseInt(targetPercentage.toFixed(0));
    const duration = 2000; // 2 seconds
    const intervalTime = 30;
    const steps = duration / intervalTime;
    const increment = targetNumber / steps;

    const counter = setInterval(() => {
      currentNumber += increment;
      if (currentNumber >= targetNumber) {
        currentNumber = targetNumber;
        clearInterval(counter);
      }
      const labelText = Math.floor(currentNumber) + '% dos ingressos vendidos a R$17,00';
      text.textContent = labelText;
      if (textFloat) textFloat.textContent = labelText;
      if (textOffer) textOffer.textContent = labelText;
    }, intervalTime);
  }
}

function getProgressPercentage() {
  const now = new Date();
  const currentDay = now.getDay();
  
  const lastMonday = new Date(now);
  const diffToMonday = currentDay === 0 ? 6 : currentDay - 1;
  lastMonday.setDate(now.getDate() - diffToMonday);
  lastMonday.setHours(0, 0, 0, 0);

  const totalMs = 7 * 24 * 60 * 60 * 1000;
  const passedMs = now.getTime() - lastMonday.getTime();

  let percentage = (passedMs / totalMs) * 100;
  if (percentage < 0) percentage = 0;
  if (percentage > 100) percentage = 100;

  let ticketsSoldPercentage = percentage;
  if (ticketsSoldPercentage < 15) ticketsSoldPercentage = 15;

  return ticketsSoldPercentage;
}

document.addEventListener('DOMContentLoaded', () => {
  const progressTrigger = document.querySelector('.progress-trigger');
  
  if (progressTrigger && window.IntersectionObserver) {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        animateProgressBar(getProgressPercentage());
        observer.disconnect();
      }
    }, { threshold: 0.1 });
    observer.observe(progressTrigger);
  } else {
    animateProgressBar(getProgressPercentage());
  }

  // ==========================================
  // GUARANTEE REVEAL (SCROLL)
  // ==========================================
  const guaranteeSection = document.querySelector('.guarantee-reveal-section');
  if (guaranteeSection) {
    window.addEventListener('scroll', () => {
      const rect = guaranteeSection.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // Slower progress
      let progress = (windowHeight - rect.top) / (windowHeight * 1.5);
      if (progress < 0) progress = 0;
      
      let radius = progress * 75;
      
      // Cap at 55% to prevent it from covering the entire screen,
      // leaving a "white circle" or white background around it
      if (radius > 55) radius = 55;
      
      guaranteeSection.style.clipPath = `circle(${radius}% at 50% 50%)`;
      
      if (progress > 0.25) {
        guaranteeSection.classList.add('is-visible');
      }
    });
    // Trigger on load just in case
    window.dispatchEvent(new Event('scroll'));
  }
});

