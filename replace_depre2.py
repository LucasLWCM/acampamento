import re

with open('depre/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# BLOCO 5: ENTREGÁVEIS E SELOS
html = re.sub(
    r'<h2 class="entregaveis-cabecalho">.*?</h2>',
    '<h2 class="entregaveis-cabecalho">EM <b>1 DIA DE IMERSÃO AO VIVO</b>, VOCÊ VAI EXECUTAR E SAIR COM:</h2>',
    html, flags=re.DOTALL
)

ent_itens = [
    "<b>Mapeie tudo o que foge do seu controle.</b> Passe pelo filtro prático de Epicteto para estancar a dor sufocante e parar de perder a paz com o que não pode ser mudado.",
    "<b>Construa o seu Círculo de Proteção Mental.</b> Pratique a separação diária das suas preocupações para parar de lutar contra o impossível e recuperar a energia que a exaustão roubou de você.",
    "<b>Treine a sua mente contra expectativas irreais.</b> Aplique a técnica da premeditação de Sêneca para blindar o seu coração das decepções e parar de sofrer pelas atitudes e opiniões dos outros.",
    "<b>Resgate a vontade de viver com Amor Fati.</b> Use os ensinamentos do imperador Marco Aurélio para sair do piloto automático e transformar a dor em força motriz, sem precisar virar uma pedra.",
    "<b>Reorganize o peso que você carrega em silêncio.</b> Crie um plano de alívio emocional para que você seja um porto seguro real para a sua família, sem precisar engolir a própria angústia.",
    "<b>Saia com o seu Guia do Recomeço pronto.</b> Leve o passo a passo exato das Leis do Estoicismo, método validado por 3.000 alunos, para reconstruir a sua rotina diária com absoluta dignidade."
]

ent_html = ""
for i, item in enumerate(ent_itens):
    delay = i * 150
    ent_html += f'        <li class="card-entregavel card-fade" style="transition-delay: {delay}ms"><div class="card-ent-check"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7" /></svg></div><p>{item}</p></li>\n'

html = re.sub(
    r'<ul class="entregaveis-lista">.*?</ul>',
    '<ul class="entregaveis-lista">\n' + ent_html + '      </ul>',
    html, flags=re.DOTALL
)

# Selos
selos_html = """      <div class="selos-grid">
        <div class="selo selo-fade" style="transition-delay: 0ms">
          <img src="../assets/images/Icons-2.svg" alt="Selo 1" width="32" height="32" loading="lazy">
          <div>
            <h5 class="selo-titulo">Prática <span class="selo-bold">direta ao ponto</span></h5>
          </div>
        </div>
        <div class="selo selo-fade" style="transition-delay: 100ms">
          <img src="../assets/images/Icons-1.svg" alt="Selo 2" width="32" height="32" loading="lazy">
          <div>
            <h5 class="selo-titulo"><span class="selo-bold">Material de apoio</span> exclusivo</h5>
          </div>
        </div>
        <div class="selo selo-fade" style="transition-delay: 200ms">
          <img src="../assets/images/Icons-3.svg" alt="Selo 3" width="32" height="32" loading="lazy">
          <div>
            <h5 class="selo-titulo">Acesso à <span class="selo-bold">Web-série Um Dia Com Marco Aurélio</span></h5>
            <p class="selo-desc">De R$ 29,90 por R$ 00,00</p>
          </div>
        </div>
        <div class="selo selo-fade" style="transition-delay: 300ms">
          <img src="../assets/images/Icons-3.svg" alt="Selo 4" width="32" height="32" loading="lazy">
          <div>
            <h5 class="selo-titulo">Acesso à <span class="selo-bold">Gravação da Palestra: A vida é pra já</span></h5>
            <p class="selo-desc">De R$ 47,00 por R$ 00,00</p>
          </div>
        </div>
      </div>"""

html = re.sub(
    r'<div class="selos-grid">.*?</div>\s*</div>\s*</section>',
    selos_html + '\n    </div>\n  </section>',
    html, flags=re.DOTALL
)

# BLOCO 6: MÉTODO
html = re.sub(
    r'<h2 class="metodo-titulo">.*?</h2>',
    '<h2 class="metodo-titulo">Como funciona a <b>nossa imersão?</b></h2>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p class="metodo-texto">.*?</p>',
    '<p class="metodo-texto">A Imersão nasceu das <b>Leis do Estoicismo</b>, um método claro de reestruturação emocional. Esse é o exato caminho que o Rafa Barbosa aplicou nele mesmo. Hoje, a estrutura já foi validada ao longo de <b>10 anos de experiência com mais de 3.000 alunos.</b></p>',
    html, flags=re.DOTALL
)

# Inserir .pilares-legenda
html = re.sub(
    r'(<picture class="ilustracao-fade">\s*<img src="\.\./assets/images/calma\.webp".*?</picture>)',
    r'\1\n    <p class="pilares-legenda">A mente humana é como um jardim que precisa ser podado diariamente para não ser tomado por ervas daninhas.</p>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h2 class="pilares-titulo">.*?</h2>',
    '<h2 class="pilares-titulo">Os 5 pilares do método <b>C.A.L.M.A.</b> na prática:</h2>',
    html, flags=re.DOTALL
)

pilares = [
    ("Consciência", "Mapeia a sua dor sufocante e o choro incontrolável, para você lidar com o sofrimento sem ser destruída."),
    ("Aceitação", "Separa a sua saudade das coisas que são incontroláveis, poupando você da exaustão inútil de tentar mudar o passado."),
    ("Limites", "Blinda a sua mente sem que você precise se tornar inerte, morna ou fria para evitar uma nova dor."),
    ("Momento Presente", "Substitui o vazio diário pela capacidade de olhar para trás com calma e tirar apenas aprendizado de tudo."),
    ("Ação", "Reorganiza a sua rotina no meio do caos, permitindo que você passe pelas dificuldades da vida serena e consciente.")
]

pil_html = ""
nums = ["I", "II", "III", "IV", "V"]
for i, (nome, desc) in enumerate(pilares):
    delay = i * 120
    pil_html += f'''        <li class="pilar-fade" style="transition-delay: {delay}ms">
          <span class="pilar-numeral">{nums[i]}</span>
          <h3 class="pilar-nome">{nome}</h3>
          <span class="pilar-desc">{desc}</span>
        </li>\n'''

html = re.sub(
    r'<ul class="pilares-lista">.*?</ul>',
    '<ul class="pilares-lista">\n' + pil_html + '      </ul>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h3 class="pilares-soma">.*?</h3>',
    '<h3 class="pilares-soma">Na imersão, você vai aplicar os primeiros passos desse método e sair com o mapa completo para continuar a reconstrução da sua rotina.</h3>',
    html, flags=re.DOTALL
)

# BLOCO 7: OFERTA
html = re.sub(
    r'<h3 class="oferta-pergunta">.*?</h3>',
    '<h3 class="oferta-pergunta">Agora você deve estar calculando quanto custa participar deste evento ao vivo.</h3>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p>Você receberá <b class="dest-verde">.*?apenas</p>',
    '<p>Você receberá <b class="dest-verde">o roteiro exato para lidar com a dor sufocante sem ser destruída.</b> Somando cursos teóricos, aplicativos de meditação e livros de filosofia, você investiria facilmente <b class="dest-terracota">R$ 567.</b></p>\n        <p>Mas o meu objetivo é remover qualquer obstáculo financeiro que te impeça de recomeçar hoje. Para que o dinheiro não justifique continuar sobrevivendo no automático, liberei um valor puramente simbólico. Você pode garantir seu ingresso para o evento por apenas</p>',
    html, flags=re.DOTALL
)

cronograma_itens = [
    ("09:00 - 10:30", "A dor sufocante e o choro", "Mapeie o seu sofrimento para separar o que é real das ilusões da sua cabeça.", "<b>Exercício:</b> Construção da sua lista visual de eliminação de medos."),
    ("10:30 - 12:00", "A exaustão de tentar controlar tudo", "Pare de gastar a sua energia vital lutando contra o passado que não pode mudar.", "<b>Exercício:</b> Montagem do seu filtro de controle para perdas repentinas."),
    ("12:00 - 13:30", "Pausa para o almoço", "", ""),
    ("13:30 - 15:30", "O medo de virar pessoa fria", "Blinde sua mente contra o julgamento sem precisar perder a sua empatia humana.", "<b>Exercício:</b> Dinâmica prática de limites usando os ensinamentos estoicos diários."),
    ("15:30 - 18:00", "O fim da vida no automático", "Substitua o vazio diário pelo poder do silêncio para encontrar paz no meio do caos.", "<b>Exercício:</b> Construção passo a passo do seu Guia do Recomeço.")
]

crono_html = ""
for (hora, titulo, desc, ex) in cronograma_itens:
    crono_html += f'''        <div class="crono-bloco">
          <div class="crono-pilula"><span class="crono-hora">{hora}</span>
            <h5>{titulo}</h5>
          </div>\n'''
    if desc: crono_html += f'          <p class="crono-desc">{desc}</p>\n'
    if ex: crono_html += f'          <p class="crono-exercicio">{ex}</p>\n'
    crono_html += '        </div>\n'

html = re.sub(
    r'(<h4 class="crono-data">.*?</h4>\s*)<div class="crono-bloco">.*?(<p class="crono-nota">)',
    r'\1' + crono_html + r'        \2',
    html, flags=re.DOTALL
)

# BLOCO 8: SOBRE
html = re.sub(
    r'<div class="sobre-texto">.*?</div>\s*<div class="sobre-numeros">',
    '<div class="sobre-texto">\n          <span class="sobre-rotulo">Rafa Barbosa</span>\n          <h2 class="sobre-titulo">Quem será o seu mentor neste Roteiro da Mente Calma?</h2>\n          <h5>Rafa Barbosa era um engenheiro bem-sucedido que vivia a mesma dor sufocante que você. Ele acreditava que controlar cada detalhe do futuro e ganhar bem garantiria uma vida segura.</h5>\n          <h5>Mas uma crise silenciosa desmoronou essas certezas de controle. Apesar do trabalho puxado, ele acordava sem nenhum ânimo e não suportava o vazio da própria rotina.</h5>\n          <h5>Foi no fundo dessa exaustão que ele usou o estoicismo para lidar com o sofrimento sem ser destruído. Ao recuperar a sua lucidez e paz interior, decidiu estruturar e compartilhar essa base sólida.</h5>\n          <h5>Hoje, como professor de filosofia, ele já orientou <b>mais de 100 mil pessoas</b> pelo Brasil. Ele cobra um valor simbólico para remover qualquer barreira financeira do seu recomeço. A missão dele é provar que você pode superar qualquer crise de forma serena e consciente.</h5>\n        </div>\n        <div class="sobre-numeros">',
    html, flags=re.DOTALL
)

html = html.replace('?src=ansiedade', '?src=depressao')

with open('depre/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
