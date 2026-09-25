/**
 * ==========================================================================
 * ESTOICISMO CONTEMPORÂNEO - MOTION E INTERAÇÕES
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Reveal Animations (Fade Up)
  const revealElements = document.querySelectorAll('.reveal-up');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        // Stop observing once revealed to improve performance
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -10% 0px', // Trigger slightly before it hits bottom
    threshold: 0.1
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // 2. Timeline Progression (Mecanismo e outras jornadas)
  const timelineSteps = document.querySelectorAll('.mechanism-step, .ident-word');
  
  const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Quando entra no centro da tela (aprox)
        entry.target.classList.add('active');
      } else {
        // Opcional: remover active quando sai da tela (se quiser que seja scroll-driven reverso)
        // entry.target.classList.remove('active');
      }
    });
  }, {
    root: null,
    rootMargin: '-40% 0px -40% 0px', // Foca bem no centro da viewport
    threshold: 0
  });

  timelineSteps.forEach(step => timelineObserver.observe(step));

  // 3. FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  
  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    
    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      
      // Fecha todos
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

  // Optimize performance: remove listener se não for mais necessário
  // A classe scroll-behavior no HTML cuida do scroll suave pros CTAs.
  
  // ==========================================
  // FLOATING CTA LOGIC
  // ==========================================
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
      const labelText = Math.floor(currentNumber) + '% das vagas preenchidas a R$17,00';
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
});
