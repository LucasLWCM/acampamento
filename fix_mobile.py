import os

def fix_mobile_png(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('Noticias_mobile.png', 'Noticias_mobile.webp')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_mobile_png('depre/index.html')
fix_mobile_png('depre-2/index.html')

