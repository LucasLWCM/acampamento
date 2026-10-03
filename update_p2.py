import re

file_path = 'impulso-p2/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Hero button
content = re.sub(
    r'<div class="hero-direita">\s*<img class="hero-foto"[^>]*>\s*<a class="btn-hero" href="#oferta">.*?</div>\s*</div>',
    '<div class="hero-direita">\n        <img class="hero-foto" src="../assets/images/rafa_hero_paz.webp" alt="Rafael Paz" fetchpriority="high"\n          decoding="async">\n      </div>',
    content,
    flags=re.DOTALL
)

# 2. Remove Crença button
content = re.sub(
    r'<a class="btn-hero" href="#oferta" style="margin-top: 2rem;">.*?</a>\s*</div>',
    '</div>',
    content
)

# 3. Update main checkout src
content = content.replace('?src=ansiedade', '?src=impulso-p2')

# 4. Update final CTA checkout link
content = content.replace(
    '<a class="btn-compra cta-btn" href="#preco">',
    '<a class="btn-compra cta-btn" href="https://checkout.thebank.com.br/7510485087637504000?src=impulso-p2">'
)

# 5. Update floating button href in HTML
content = content.replace(
    '<a class="btn-hero btn-floating" href="#oferta">',
    '<a class="btn-hero btn-floating" href="https://checkout.thebank.com.br/7510485087637504000?src=impulso-p2">'
)

# 6. Rewrite floating CTA JS logic
old_js_pattern = r'// Lógica Floating CTA.*?window\.dispatchEvent\(new Event\(\'scroll\'\)\);\s*}'
new_js = '''// Lógica Floating CTA
      const ofertaSection = document.getElementById('oferta');
      const floatingCta = document.getElementById('floating-cta');
      const floatingBtn = floatingCta ? floatingCta.querySelector('.btn-floating') : null;

      if (ofertaSection && floatingCta && floatingBtn) {
        window.addEventListener('scroll', () => {
          const ofertaRect = ofertaSection.getBoundingClientRect();
          if (ofertaRect.bottom < 0) {
            floatingCta.classList.add('visible');
            floatingBtn.href = 'https://checkout.thebank.com.br/7510485087637504000?src=impulso-p2';
          } else {
            floatingCta.classList.remove('visible');
          }
        }, { passive: true });
        window.dispatchEvent(new Event('scroll'));
      }'''
content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to impulso-p2 successfully.")
