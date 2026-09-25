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
    // ==========================================
    // DOBRA 2 — CAMINHO
    // ==========================================

    // Contador Animado
    const contador = document.getElementById('contador-afastamentos');
    const triggerContador = document.getElementById('trigger-contador');
    let contadorRodou = false;

    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
            const current = Math.floor(easeProgress * (end - start) + start);
            obj.innerHTML = current.toLocaleString('pt-BR');
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    if (triggerContador && contador) {
        const contadorObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !contadorRodou) {
                contadorRodou = true;
                animateValue(contador, 0, 546254, 2500);
            }
        }, { threshold: 0.5 });
        contadorObserver.observe(triggerContador);
    }

    // Pictograma
    const triggerPictograma = document.getElementById('trigger-pictograma');
    let pictogramaRodou = false;
    
    if (triggerPictograma) {
        const picObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !pictogramaRodou) {
                pictogramaRodou = true;
                const bonecos = document.querySelectorAll('#pictograma-bonecos .boneco');
                setTimeout(() => {
                    for(let i=0; i<7; i++) {
                        bonecos[i].classList.add('acende');
                    }
                    setTimeout(() => {
                        for(let i=0; i<5; i++) {
                            bonecos[i].classList.add('nunca-ajuda');
                        }
                        document.getElementById('legenda-bonecos').classList.add('visible');
                    }, 1200);
                }, 400);
            }
        }, { threshold: 0.5 });
        picObserver.observe(triggerPictograma);
    }

    // Ciclo Scroll Diagrama
    const passoTriggers = document.querySelectorAll('.passo-trigger');
    const anelProgresso = document.getElementById('passos-anel-progresso');
    
    if (passoTriggers.length > 0) {
        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const step = parseInt(entry.target.getAttribute('data-step'));
                    
                    // Atualiza nós
                    for(let i=1; i<=4; i++) {
                        const node = document.getElementById(`node-${i}`);
                        if (node) {
                            if (i <= step) node.classList.add('active');
                            else node.classList.remove('active');
                        }
                    }

                    // Atualiza Anel (628 é a circunferência total do raio 100)
                    if (anelProgresso) {
                        const pct = step / 4;
                        const offset = 628 - (628 * pct);
                        anelProgresso.style.strokeDashoffset = offset;
                    }
                }
            });
        }, { threshold: 0.2, rootMargin: "-10% 0px -40% 0px" });

        passoTriggers.forEach(t => scrollObserver.observe(t));
    }

    // Verbos Gigantes
    const verbosTrigger = document.getElementById('verbos-trigger');
    let verbosRodou = false;

    if (verbosTrigger) {
        const verbosObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !verbosRodou) {
                verbosRodou = true;
                setTimeout(() => document.getElementById('verbo-1').classList.add('visible'), 200);
                setTimeout(() => document.getElementById('verbo-2').classList.add('visible'), 1200);
                setTimeout(() => {
                    document.getElementById('verbo-3').classList.add('visible');
                    // Quebra o anel lá em cima
                    const anelBg = document.getElementById('passos-anel-bg');
                    if(anelBg) {
                        anelBg.style.strokeDasharray = '628';
                        anelBg.style.strokeDashoffset = '62';
                        anelBg.style.transition = 'stroke-dashoffset 1s ease';
                    }
                    if(anelProgresso) anelProgresso.style.display = 'none';
                }, 2200);
            }
        }, { threshold: 0.5 });
        verbosObserver.observe(verbosTrigger);
    }

});
