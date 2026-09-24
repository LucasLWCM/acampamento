/* ==========================================================================
   SCRIPTS GLOBAIS - ANIMAÇÕES E INTERAÇÕES
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Animação Fade-in ao Rolar a Página (Intersection Observer)
  const observerOptions = {
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  console.log('⚡ Projeto Lc Pago carregado com sucesso!');
});
