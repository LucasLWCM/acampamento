import re

with open('impulso/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Topbar
html = re.sub(r'<h4>EXCLUSIVO PARA QUEM ESTÁ EXAUSTO DE <b>.*?</b></h4>', r'<h4>O PRIMEIRO PASSO PARA QUEM ESTÁ CANSADO DE <b>PERDER A CABEÇA</b></h4>', html)

# Replace H1
html = re.sub(r'<h1><b>Resgate sua paz em 1 dia</b> com o <b>Roteiro da Mente Calma</b> e pare de sofrer com a ansiedade\.</h1>', r'<h1><b>Pare de explodir com pessoas desrespeitosas</b> e <b>retome o controle absoluto</b> da sua paz de espírito em 1 dia.</h1>', html)

with open('impulso/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
