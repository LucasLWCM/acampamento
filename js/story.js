// Scroll Storytelling (Apple-style)
document.addEventListener('DOMContentLoaded', () => {
  const scrollSection = document.getElementById('story-demo');
  if (scrollSection) {
    window.addEventListener('scroll', () => {
      const rect = scrollSection.getBoundingClientRect();
      const maxScroll = rect.height - window.innerHeight;
      
      if (rect.top <= 0 && rect.bottom >= window.innerHeight) {
        let progress = Math.abs(rect.top) / maxScroll;
        let step = 0;
        
        if (progress > 0.05) step = 1;
        if (progress > 0.25) step = 2;
        if (progress > 0.45) step = 3;
        if (progress > 0.65) step = 4;
        if (progress > 0.85) step = 5;
        
        scrollSection.setAttribute('data-step', step);
      } else if (rect.top > 0) {
        scrollSection.setAttribute('data-step', 0);
      } else {
        scrollSection.setAttribute('data-step', 5);
      }
    });
  }
});
