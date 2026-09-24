import re

def optimize_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    def replace_img(match):
        tag = match.group(0)
        if 'Logo2' in tag or 'Logo_evento' in tag or 'hero' in tag:
            if 'fetchpriority' not in tag:
                tag = tag.replace('<img', '<img fetchpriority="high"')
            return tag
        
        if 'loading=' not in tag:
            tag = tag.replace('<img', '<img loading="lazy" decoding="async"')
        return tag

    new_html = re.sub(r'<img[^>]+>', replace_img, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

optimize_html('p3/index.html')
try:
    optimize_html('index.html')
except:
    pass
print('Done injecting lazy loading attributes.')
