import re

file_path = 'estoicismo-p2/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Hero button
content = re.sub(
    r'<a class="btn-hero" href="#oferta">.*?</a>',
    '',
    content
)

# 2. Update main checkout src
content = content.replace('?src=estoicismo', '?src=estoicismo-p2')

# 3. Update bottom CTA checkout link
content = content.replace(
    '<a class="btn-compra cta-btn" href="#preco">',
    '<a class="btn-compra cta-btn" href="https://checkout.thebank.com.br/7510485087637504000?src=estoicismo-p2">'
)

# 4. Update floating button href in HTML
content = content.replace(
    '<a class="btn-hero btn-floating" href="#oferta">',
    '<a class="btn-hero btn-floating" href="https://checkout.thebank.com.br/7510485087637504000?src=estoicismo-p2">'
)

# 5. Rewrite floating CTA JS logic to only appear after #oferta
old_js_pattern = r'// L.gica Floating CTA.*?window\.dispatchEvent\(new Event\(\'scroll\'\)\);\s*}'
new_js = '''// Lógica Floating CTA
      const ofertaSection = document.getElementById('oferta');
      const floatingCta = document.getElementById('floating-cta');
      const floatingBtn = floatingCta ? floatingCta.querySelector('.btn-floating') : null;

      if (ofertaSection && floatingCta && floatingBtn) {
        window.addEventListener('scroll', () => {
          const ofertaRect = ofertaSection.getBoundingClientRect();
          if (ofertaRect.bottom < 0) {
            floatingCta.classList.add('visible');
            floatingBtn.href = 'https://checkout.thebank.com.br/7510485087637504000?src=estoicismo-p2';
          } else {
            floatingCta.classList.remove('visible');
          }
        }, { passive: true });
        window.dispatchEvent(new Event('scroll'));
      }'''
content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("P2 applied successfully")
