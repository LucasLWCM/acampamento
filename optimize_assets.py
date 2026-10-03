import os
import re

png1 = 'assets/images/luto_noticia.png'
png2 = 'assets/images/Noticias_mobile.png'

if os.path.exists(png1):
    os.remove(png1)
if os.path.exists(png2):
    os.remove(png2)

def optimize_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change luto_noticia.png to .webp
    html = html.replace('luto_noticia.png', 'luto_noticia.webp')

    # Ensure hero-foto has fetchpriority="high" and decoding="async"
    # Actually, they already have it: <img class="hero-foto" src="../assets/images/rafa_hero_paz.webp" alt="Rafa Barbosa" fetchpriority="high" decoding="async">
    # Ensure other images have loading="lazy" (the original ansiedade already did this, but let's check luto_noticia)
    html = html.replace('<img src="../assets/images/luto_noticia.webp" alt="Manchetes de veículos sobre ansiedade" loading="lazy" decoding="async">', 
                        '<img src="../assets/images/luto_noticia.webp" alt="Manchetes de veículos sobre luto" loading="lazy" decoding="async">')
    # Or generically
    html = html.replace('luto_noticia.png', 'luto_noticia.webp')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

optimize_html('depre/index.html')
optimize_html('depre-2/index.html')

