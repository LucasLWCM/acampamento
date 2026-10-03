import re

with open('impulso/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace css/ with ../css/
html = re.sub(r'(href|src)="css/', r'\1="../css/', html)
# Replace assets/ with ../assets/
html = re.sub(r'(href|src)="assets/', r'\1="../assets/', html)
# Replace js/ with ../js/
html = re.sub(r'(href|src)="js/', r'\1="../js/', html)

with open('impulso/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
