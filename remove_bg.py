from rembg import remove
from PIL import Image

input_path = 'assets/images/IMG_3921.JPG'
output_path = 'assets/images/rafael-hero-nobg.png'

print('Removing background...')
inp = Image.open(input_path)
out = remove(inp)
out.save(output_path)
print('Background removed.')
