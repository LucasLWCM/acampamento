import re

with open('depre/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# BLOCO 4: CRENÇA + SINTOMAS
html = re.sub(
    r'<h3 class="crenca-grande">.*?</h3>',
    '<h3 class="crenca-grande">Te contaram que <b>engolir o choro</b>, <b>ser forte o tempo todo</b> e <b>viver sem expectativas</b> era o único jeito de suportar as grandes perdas da vida, mas esqueceram de te contar algo sobre a sua paz interior...</h3>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h4 class="crenca-menor">.*?</h4>',
    '<h4 class="crenca-menor">A verdadeira cura da sua angústia nasce da coragem de aceitar a realidade e <b>focar a sua energia apenas naquilo que você pode controlar.</b><br><br>Mas você não consegue perceber isso hoje, pois a sua mente virou um jardim tomado por ervas daninhas, onde você gasta toda a sua força tentando consertar o passado e lutando contra o impossível.<br><br>E é exatamente por carregar esse peso invisível que você começa a notar os sinais de que a sua saúde emocional está desmoronando:</h4>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h3 class="crenca-cabecalho">.*?</h3>',
    '<h3 class="crenca-cabecalho"><b>Há quanto tempo você:</b></h3>',
    html, flags=re.DOTALL
)

lista_itens = [
    "acorda com uma DOR SUFOCANTE e um choro incontrolável?",
    "tenta controlar o impossível e termina o seu dia exausta?",
    "se sente inerte e morna por tentar viver sem expectativas?",
    "sofre demais com as atitudes e opiniões de outras pessoas?",
    "engole a angústia em silêncio para parecer forte para a família?",
    "perde a paz remoendo perdas que estão totalmente fora do controle?",
    "ignora os sinais de esgotamento que a sua mente grita?",
    "sente o coração sangrar e SOBREVIVE no automático todos os dias?"
]

lista_html = ""
for i, item in enumerate(lista_itens):
    delay = i * 80
    lista_html += f'          <li class="checklist-fade" style="transition-delay: {delay}ms"><span class="crenca-icone"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7" /></svg></span><span class="crenca-item">{item}</span></li>\n'

html = re.sub(
    r'<ul class="crenca-lista">.*?</ul>',
    '<ul class="crenca-lista">\n' + lista_html + '        </ul>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h4 class="crenca-fechamento">.*?</h4>',
    '<h4 class="crenca-fechamento">Já fez as contas? Talvez há meses, ou até mesmo anos, você viva exatamente assim.<br><br><b>CHEGA DE NORMALIZAR ESSA DOR.</b></h4>',
    html, flags=re.DOTALL
)

html = html.replace('Quero resgatar minha paz mental', 'Quero construir meu recomeço')

with open('depre/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
