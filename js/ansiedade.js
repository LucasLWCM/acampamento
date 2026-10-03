document.addEventListener('DOMContentLoaded', () => {
  // Configuração do IntersectionObserver para a animação Reveal
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Se for um item de lista ou estiver dentro de um grupo sequencial
        if (entry.target.hasAttribute('data-sequence')) {
          const delay = parseInt(entry.target.getAttribute('data-sequence')) * 80;
          setTimeout(() => {
            entry.target.classList.add('active');
          }, delay);
        } else {
          entry.target.classList.add('active');
        }
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const revealElements = document.querySelectorAll('.reveal');
  revealElements.forEach(el => observer.observe(el));
});
