
from PIL import Image
import os

hero = 'assets/images/hero_principal.webp'
logo = 'assets/images/Logo2.webp'

if os.path.exists(hero):
    with Image.open(hero) as img:
        img = img.resize((800, 400), Image.Resampling.LANCZOS)
        img.save(hero, 'WEBP', quality=85)

if os.path.exists(logo):
    with Image.open(logo) as img:
        img = img.resize((400, 266), Image.Resampling.LANCZOS)
        img.save(logo, 'WEBP', quality=85)

print('Resized!')

