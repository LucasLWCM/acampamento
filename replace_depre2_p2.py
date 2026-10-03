import re

with open('depre-2/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update checkout links
html = html.replace('?src=depressao', '?src=depre-2')

# 2. Update CTA final link
html = html.replace('<a class="btn-compra cta-btn" href="#preco">', '<a class="btn-compra cta-btn" href="https://checkout.thebank.com.br/7510485087637504000?src=depre-2">')

# 3. Remove hero button and counter
html = re.sub(
    r'<a class="btn-hero" href="#oferta">Comprar ingresso \| LOTE 1</a>\s*<p class="hero-depor">De <s>R\$ 97,00</s> por apenas <b>R\$ 24,00</b></p>\s*<div class="contador">.*?</div>\s*</div>\s*</section>',
    r'</div>\n    </section>',
    html,
    flags=re.DOTALL
)

# 4. Modify JS logic for floating-cta
js_old = '''
      // Lógica Floating CTA
      const heroButton = document.querySelector('.hero-direita .btn-hero');
      const ofertaSection = document.getElementById('oferta');
      const floatingCta = document.getElementById('floating-cta');
      const floatingBtn = floatingCta ? floatingCta.querySelector('.btn-floating') : null;

      if (heroButton && ofertaSection && floatingCta && floatingBtn) {
        window.addEventListener('scroll', () => {
          const heroRect = heroButton.getBoundingClientRect();
          const ofertaRect = ofertaSection.getBoundingClientRect();

          if (heroRect.bottom < 0) {
            // Antes da seção de oferta
            if (ofertaRect.top > window.innerHeight) {
              floatingCta.classList.add('visible');
              floatingBtn.href = '#oferta';
            }
            // Depois da seção de oferta
            else if (ofertaRect.bottom < 0) {
              floatingCta.classList.add('visible');
              floatingBtn.href = 'https://checkout.thebank.com.br/7510485087637504000?src=depre-2';
            }
            // Durante a seção de oferta
            else {
              floatingCta.classList.remove('visible');
            }
          } else {
            floatingCta.classList.remove('visible');
          }
        }, { passive: true });
        // Initial check in case user loads halfway down the page
        window.dispatchEvent(new Event('scroll'));
      }
'''

js_new = '''
      // Lógica Floating CTA
      const ofertaSection = document.getElementById('oferta');
      const floatingCta = document.getElementById('floating-cta');
      const floatingBtn = floatingCta ? floatingCta.querySelector('.btn-floating') : null;

      if (ofertaSection && floatingCta && floatingBtn) {
        window.addEventListener('scroll', () => {
          const ofertaRect = ofertaSection.getBoundingClientRect();

          // Só aparece o botão DEPOIS da seção de oferta
          if (ofertaRect.bottom < 0) {
            floatingCta.classList.add('visible');
            floatingBtn.href = 'https://checkout.thebank.com.br/7510485087637504000?src=depre-2';
          } else {
            floatingCta.classList.remove('visible');
          }
        }, { passive: true });
        // Initial check in case user loads halfway down the page
        window.dispatchEvent(new Event('scroll'));
      }
'''
html = html.replace(js_old.strip(), js_new.strip())

with open('depre-2/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
