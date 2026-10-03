def fix_symbols(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Emoticons and symbols
    replacements = {
        'ðŸ›¡ï¸ ': '🛡️',
        'Â·': '·',
        'Â©': '©'
    }

    for bad, good in replacements.items():
        text = text.replace(bad, good)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed symbols in {filepath}")

fix_symbols('estoicismo/index.html')
fix_symbols('estoicismo-p2/index.html')
