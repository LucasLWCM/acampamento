def fix_mojibake(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = {
        'Ã”': 'Ô', 
        'Ã ': 'à',
        '””': '—',
    }

    for bad, good in replacements.items():
        text = text.replace(bad, good)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed {filepath}")

fix_mojibake('estoicismo/index.html')
fix_mojibake('estoicismo-p2/index.html')
