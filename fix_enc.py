def fix_encoding(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        fixed = text.encode('cp1252').decode('utf-8')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"Fixed {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

fix_encoding('estoicismo/index.html')
fix_encoding('estoicismo-p2/index.html')
