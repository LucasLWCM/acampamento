import re

with open('depre-2/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove floating-contador
html = re.sub(
    r'<div class="floating-contador">.*?</div>\s*</div>\s*<a class="btn-hero btn-floating"',
    r'<a class="btn-hero btn-floating"',
    html,
    flags=re.DOTALL
)

with open('depre-2/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
