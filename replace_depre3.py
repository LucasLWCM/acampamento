with open('depre/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css = '''
  <style>
    .pilares-legenda { max-width:560px; margin:-8px auto 24px; text-align:center; text-wrap:balance; font-family:"Montserrat",sans-serif; font-size:1.6rem; line-height:1.4; color:#697470; }
  </style>
</head>'''

html = html.replace('</head>', css)

html = html.replace('Lote 1', 'LOTE 1')

with open('depre/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
