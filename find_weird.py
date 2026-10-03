def find_weird(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    weird = set(re.findall(r'Ã.', text))
    print(f"Weird in {filepath}: {weird}")

find_weird('estoicismo-p2/index.html')
