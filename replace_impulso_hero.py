with open('impulso/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Topbar
html = html.replace('EXCLUSIVO PARA QUEM ESTÁ EXAUSTO DE <b>SOFRER POR ANTECIPAÇÃO</b>', 'O PRIMEIRO PASSO PARA QUEM ESTÁ CANSADO DE <b>PERDER A CABEÇA</b>')

# Replace H1
html = html.replace('<h1><b>Resgate sua paz em 1 dia</b> e <b>pare de sofrer com problemas</b> que só existem na sua cabeça.</h1>', '<h1><b>Pare de explodir com pessoas desrespeitosas</b> e <b>retome o controle absoluto</b> da sua paz de espírito em 1 dia.</h1>')

# Replace hero-sub (H2)
html = html.replace('<p class="hero-sub">Aprenda a separar problemas reais de invenções da cabeça. Saia deste workshop com um plano\n          prático para dominar a ansiedade sem precisar de meditações complexas.</p>', '<p class="hero-sub">Chega de viver com o "pavio curto" e perder a cabeça por impulso. Aplique o método exato para manter a sua serenidade intacta e focar apenas nas soluções.</p>')

# Replace hero-chamada (H3)
html = html.replace('<h5 class="hero-chamada"><b>Chegou a hora de se libertar</b> do que te faz viver ansioso, exausto e com a mente\n          acelerada, te afastando da sua paz e do seu equilíbrio.</h5>', '<h5 class="hero-chamada"><b>Chegou a hora de se libertar</b> do comportamento imediatista, que faz com que algo pontual acabe com o seu dia todo, te afastando da sua paz e do domínio sobre as suas próprias reações.</h5>')

with open('impulso/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
