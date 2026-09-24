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
});
