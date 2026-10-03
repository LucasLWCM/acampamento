import re

def fix_word(match):
    word = match.group(0)
    try:
        return word.encode('cp1252').decode('utf-8')
    except:
        return word

def fix_all(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find sequences of characters that contain Ã and following characters that might belong to the utf8 sequence
    # Since any cp1252 character could be part of it, we just encode/decode chunks that start with Ã and have length 2
    
    # We can just match Ã followed by ANY 1 character (since UTF-8 sequences for latin chars are 2 bytes)
    # So Ã£ is Ã and £
    text = re.sub(r'Ã.', fix_word, text)
    
    # Also handle some special cases like â€œ -> “
    text = text.replace('â€œ', '“').replace('â€', '”').replace('”\x9d', '”')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed {filepath}")

fix_all('estoicismo/index.html')
fix_all('estoicismo-p2/index.html')
