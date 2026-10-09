import re

with open('principal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# get the script block
script_match = re.search(r'(<script>\s*document\.addEventListener\("DOMContentLoaded", \(\) => \{.+?</script>)', html, re.DOTALL)
if script_match:
    script_block = script_match.group(1)

    with open('principal-p2/index.html', 'r', encoding='utf-8') as f:
        html2 = f.read()

    html2 = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded", \(\) => \{.+?</script>', script_block.replace('\\', '\\\\'), html2, flags=re.DOTALL)

    # fix preload
    html2 = html2.replace('<link rel="preload" as="image" href="../assets/images/hero_principal.webp">', '<link rel="preload" as="image" href="../assets/images/hero_principal.webp" fetchpriority="high">')

    with open('principal-p2/index.html', 'w', encoding='utf-8') as f:
        f.write(html2)
    print('Synced')
else:
    print('Not found')
