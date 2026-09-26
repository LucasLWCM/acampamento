# Documentação do Projeto: Acampamento Estoico

Este documento serve como um guia de **handoff** e documentação de estado atual do projeto para que outros agentes de IA (ou desenvolvedores) possam entender a arquitetura, o que foi feito e como continuar o trabalho sem precisar ler todos os arquivos.

## 1. Visão Geral do Projeto
O projeto é uma **Landing Page de Alta Conversão** (focada em tráfego pago) para a venda de ingressos do evento online "Acampamento Estoico" ministrado pelo Rafael Barbosa. 
O site foi construído estaticamente (HTML, CSS e JS puros), sem frameworks complexos, visando máxima velocidade e performance.

## 2. Estrutura Atual de Pastas
O repositório contém várias iterações de Landing Pages que funcionam como testes A/B (diferentes estilos e narrativas) para validar conversão:

```text
/
├── index.html           (Versão 1 - Estrutura antiga/raiz para teste A/B)
├── p2/
│   └── index.html       (Versão 2 - Estilo visual diferente para teste A/B)
├── p3/
│   └── index.html       (Versão 3 - Estilo visual diferente para teste A/B)
├── p4/
│   └── index.html       (Versão 4 - Vencedora atual, c/ Bônus da Websérie)
├── p5/
│   └── index.html       (Versão 5 - Variação exata da p4, porém SEM Bônus)
├── css/
│   ├── p4.css           (Folha de estilos otimizada, usada pela p4 e p5)
│   └── ...              (Folhas de estilos das versões anteriores: p2, p3, main, etc.)
├── js/
│   ├── p4.js            (Script otimizado, usado pela p4 e p5)
│   └── ...              (Scripts das versões anteriores)
├── assets/
│   └── images/          (Imagens de todas as versões do projeto)
├── Dockerfile           (Configuração de container NGINX)
├── nginx.conf           (Regras de GZIP e Cache para performance extrema)
├── optimize.py          (Script utilitário em Python para otimização - legado)
├── remove_bg.py         (Script utilitário em Python para remoção bg - legado)
└── DOCUMENTACAO_PROJETO.md (Este arquivo)
```

## 3. O Que Foi Realizado (Histórico Recente)
- **Construção da P4:** Foi montada uma estrutura narrativa completa de 13 dobras, focada na quebra do ciclo de raiva/ansiedade.
- **Animações e Micro-interações:** Foram incluídos gráficos interativos (SVG giratório na Hero, árvore de progresso, timeline animada) nativos, sem bibliotecas externas.
- **Variação P5:** O diretório `p5/` foi criado como um clone da `p4`, porém limpo de qualquer menção à "série de bônus do Marco Aurélio" (para ser usado quando o Lote 0 ou o bônus se encerrar).
- **Manutenção de Histórico (Teste A/B):** As versões antigas (`index.html`, `p2`, `p3`) e seus respectivos assets foram mantidos intencionalmente para fins de teste A/B.
- **Otimização de Performance (Tempo de Carregamento < 2s):**
  - Fontes (Google Fonts) configuradas com preconnect no HTML.
  - Imagens de dobras inferiores receberam `loading="lazy"`.
  - Imagens convertidas globalmente para `.webp`.
  - Configurado Servidor NGINX (via Docker e `nginx.conf`) para entregar os arquivos via GZIP (Nível 6) e headers de Cache `max-age` agressivos.

## 4. Guia Rápido de Edição para a IA

1. **Alterar Cores Globais:** 
   Se for solicitado mudar as cores, edite as variáveis CSS no topo do arquivo `css/p4.css`:
   - `--c-bg-claro`: Cor bege clara do fundo de algumas seções.
   - `--c-bg-escuro`: Cor verde escuro/musgo padrão (principal).
   - `--c-texto-claro`: Letras claras (para usar no fundo escuro).
   - `--c-texto-escuro`: Letras escuras (para usar no fundo claro).
   - `--c-ambar` e `--c-botao`: Cores de destaque (botões e detalhes).

2. **Como Editar o HTML:**
   Se precisar mexer em textos de Copy, verifique se a mudança deve se aplicar na **P4** (Com Bônus) ou na **P5** (Sem Bônus). Muitas vezes, a edição precisará ser feita em ambas as pastas (`p4/index.html` e `p5/index.html`).

3. **Arquivos Compartilhados:**
   Toda estilização e scripts lógicos (como os observadores de scroll `IntersectionObserver` da timeline ou as lógicas de expansão de FAQ) devem ser editados em **`css/p4.css`** e **`js/p4.js`**. Ambas as páginas (`p4` e `p5`) "puxam" recursos desse mesmo diretório para evitar código duplicado.

## Status Final
O projeto encontra-se limpo, otimizado e versionado no Git. O desenvolvimento base das versões com/sem bônus está fechado e pronto para tráfego.
