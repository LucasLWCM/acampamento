// JS para a P4

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Reveal Animation
    const reveals = document.querySelectorAll('.reveal');
    const revealOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, revealOptions);
    
    reveals.forEach(reveal => {
      revealObserver.observe(reveal);
    });

    // 2. Smooth Scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 3. Progress Bar Animation
    setTimeout(() => {
        const progressBar = document.getElementById('lote-0-progress');
        if (progressBar) {
            progressBar.style.width = '65%';
        }
    }, 500);

    // 4. SVG Cycle Interaction
    const palavras = document.querySelectorAll('.ciclo-palavra');
    const brasaGroup = document.getElementById('brasa-group');
    const anel = document.getElementById('anel');
    const pergunta = document.getElementById('ciclo-pergunta');
    const resultado = document.getElementById('ciclo-resultado');

    if (palavras.length > 0) {
        palavras.forEach(palavra => {
            palavra.addEventListener('click', () => {
                // Remove active de todas e reseta
                palavras.forEach(p => p.classList.remove('active'));
                
                // Adiciona active na clicada
                palavra.classList.add('active');

                // Para a animação da brasa e centraliza
                brasaGroup.classList.remove('anim-rodar');
                brasaGroup.style.display = 'none'; // Some com a brasa rodando, poderia também só pausar. 

                // Abre o anel (quebra o ciclo)
                // O anel tem stroke-dasharray = 628. Ao colocar dashoffset, ele abre um gap.
                anel.style.strokeDashoffset = '62'; 

                // Esconde pergunta, mostra resultado
                pergunta.style.display = 'none';
                
                const word = palavra.getAttribute('data-word').toLowerCase();
                const pct = palavra.getAttribute('data-pct');
                
                // Gramática do texto
                let acao = word;
                if (word === 'travo') acao = 'travam';
                else if (word === 'explodo') acao = 'explodem';
                else if (word === 'fujo') acao = 'fogem';
                else if (word === 'me culpo') acao = 'se culpam';

                resultado.textContent = `${pct}% dos alunos também ${acao}.`;
                resultado.classList.add('visible');
            });
        });
    }

});
