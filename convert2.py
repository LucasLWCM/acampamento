import os
try:
    from PIL import Image
    files = [
        'bkhero.png',
        'bk_hero_mobile.png'
    ]
    for f in files:
        in_path = os.path.join('assets', 'images', f)
        out_path = os.path.join('assets', 'images', f.replace('.png', '.webp'))
        if os.path.exists(in_path):
            img = Image.open(in_path)
            img.save(out_path, 'webp', quality=80)
            print(f'Convertido {f}')
        else:
            print(f'Arquivo não encontrado: {in_path}')
except Exception as e:
    print('Erro: ', e)
