import re
from PIL import Image
import os

with open('principal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    img_tag = match.group(0)
    
    # If it already has width and height, skip
    if 'width=' in img_tag and 'height=' in img_tag:
        return img_tag
        
    src_match = re.search(r'src="([^"]+)"', img_tag)
    if not src_match:
        return img_tag
        
    src = src_match.group(1)
    file_path = src.replace('../', '')
    
    try:
        if os.path.exists(file_path):
            with Image.open(file_path) as img:
                width, height = img.size
                
                # Add fetchpriority to hero
                if 'hero_principal.webp' in src:
                    new_img = img_tag.replace('<img ', f'<img fetchpriority="high" width="{width}" height="{height}" ')
                else:
                    new_img = img_tag.replace('<img ', f'<img width="{width}" height="{height}" ')
                return new_img
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
    
    return img_tag

new_html = re.sub(r'<img [^>]+>', replacer, html)

# Remove loading="lazy" from hero if it has it
hero_lazy = re.search(r'<img[^>]*src="[^"]*hero_principal\.webp"[^>]*loading="lazy"[^>]*>', new_html)
if hero_lazy:
    hero_img = hero_lazy.group(0)
    new_hero_img = hero_img.replace('loading="lazy" ', '').replace('loading="lazy"', '')
    new_html = new_html.replace(hero_img, new_hero_img)

with open('principal/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Also apply it to principal-p2 to keep it optimized
with open('principal-p2/index.html', 'r', encoding='utf-8') as f:
    html2 = f.read()
new_html2 = re.sub(r'<img [^>]+>', replacer, html2)
hero_lazy2 = re.search(r'<img[^>]*src="[^"]*hero_principal\.webp"[^>]*loading="lazy"[^>]*>', new_html2)
if hero_lazy2:
    hero_img2 = hero_lazy2.group(0)
    new_hero_img2 = hero_img2.replace('loading="lazy" ', '').replace('loading="lazy"', '')
    new_html2 = new_html2.replace(hero_img2, new_hero_img2)
with open('principal-p2/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html2)

print('Done!')
