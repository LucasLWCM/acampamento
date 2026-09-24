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

  // 3. Sticky CTA Logic (Aparece apenas após rolar pela oferta)
  const stickyCta = document.getElementById('sticky-cta');
  const offerSection = document.getElementById('oferta');
  
  if (stickyCta && offerSection) {
    const stickyObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        // Se a seção de oferta passou (isIntersecting false e boundingClientRect.top < 0)
        // Isso significa que rolamos para baixo dela.
        if (!entry.isIntersecting && entry.boundingClientRect.top < 0) {
          stickyCta.classList.add('visible');
        } else {
          stickyCta.classList.remove('visible');
        }
      });
    }, {
      root: null,
      threshold: 0
    });
    
    stickyObserver.observe(offerSection);
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
