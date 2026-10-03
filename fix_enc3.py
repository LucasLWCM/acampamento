def fix_mojibake(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = {
        'Ã£': 'ã', 'Ã©': 'é', 'Ã§': 'ç', 'Ã­': 'í', 'Ã³': 'ó', 
        'Ãª': 'ê', 'Ã¡': 'á', 'Ãº': 'ú', 'Ã¢': 'â', 'Ãµ': 'õ', 
        'Ã‰': 'É', 'Ã€': 'À', 'â€œ': '“', 'â€\x9d': '”', 'â€': '”',
        'Ã\x8d': 'Í', 'Ã\x95': 'Õ', 'Ã\x87': 'Ç', 'Ã\x8a': 'Ê',
        'Ã\x81': 'Á', 'Ã\x93': 'Ó', 'Ã\x9a': 'Ú', 'Ã\x82': 'Â',
        'Ã\x83': 'Ã', 'Ã\x89': 'É'
    }

    # Also handle some generic ones like Ã³
    for bad, good in replacements.items():
        text = text.replace(bad, good)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed {filepath}")

fix_mojibake('estoicismo/index.html')
fix_mojibake('estoicismo-p2/index.html')
