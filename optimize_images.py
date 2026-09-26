import os
from PIL import Image

def optimize_image(input_path, output_path, max_width, format='WEBP', quality=85):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return
        
    try:
        with Image.open(input_path) as img:
            # Calculate new size preserving aspect ratio
            if img.width > max_width:
                wpercent = (max_width / float(img.width))
                hsize = int((float(img.height) * float(wpercent)))
                img = img.resize((max_width, hsize), Image.Resampling.LANCZOS)
            
            # Save the image
            img.save(output_path, format, quality=quality)
            
            old_size = os.path.getsize(input_path) / (1024 * 1024)
            new_size = os.path.getsize(output_path) / (1024 * 1024)
            print(f"Optimized {os.path.basename(input_path)}: {old_size:.2f}MB -> {new_size:.2f}MB")
    except Exception as e:
        print(f"Error optimizing {input_path}: {e}")

images_to_optimize = [
    ('assets/images/rafael-hero-nobg.png', 'assets/images/rafael-hero-nobg.webp', 1200),
    ('assets/images/IMG_9309.JPEG', 'assets/images/rafa-perfil.webp', 1000),
    ('assets/images/sit-1.jpg', 'assets/images/sit-1.webp', 800),
    ('assets/images/sit-2.jpg', 'assets/images/sit-2.webp', 800),
    ('assets/images/sit-3.jpg', 'assets/images/sit-3.webp', 800),
    ('assets/images/sit-4.jpg', 'assets/images/sit-4.webp', 800)
]

for in_path, out_path, max_w in images_to_optimize:
    optimize_image(in_path, out_path, max_w)

