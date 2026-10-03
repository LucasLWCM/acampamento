const fs = require('fs');
const { execSync } = require('child_process');

const files = [
  { in: 'estoicismo_noticia.png', out: 'estoicismo_noticia.webp' },
  { in: 'estoicismo_noticia mobile.png', out: 'estoicismo_noticia_mobile.webp' }
];

files.forEach(f => {
  const input = 'assets/images/' + f.in;
  const output = 'assets/images/' + f.out;
  if (fs.existsSync(input)) {
    try {
      execSync(`npx -y sharp-cli@latest -i "${input}" -o "${output}"`);
      console.log('Convertido: ' + f.in);
      fs.unlinkSync(input);
      console.log('Apagado: ' + f.in);
    } catch (e) {
      console.log('Erro ao converter ' + f.in);
    }
  }
});
