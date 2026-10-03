with open('depre/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Risco zero: cancele em até 2 dias APÓS o evento.', 'Risco zero: cancele até 2 dias APÓS o evento.')

with open('depre/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
