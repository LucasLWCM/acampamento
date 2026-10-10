# Princípios de design — página `principal`

Proposta para revisão. Nada aqui está construído ainda.

Referência de estrutura: `udcma.rafaelbarbosaoficial.com.br/p7`.
Produto: Acampamento Estoico (17 de outubro, online e ao vivo).

---

## 1. Ideia central

**Mesmo esqueleto da p7, estímulo visual oposto.**

| | p7 (referência) | `principal` |
|---|---|---|
| Sensação | Cinema, fogo, urgência | Livro antigo, terra, firmeza |
| Temperatura | Preto + dourado + vermelho | Papel + oliva + terracota |
| Voz do título | Sans pesada, CAIXA ALTA | Serifa pesada, caixa normal |
| Forma | Pílulas, cantos redondos, brilho | Cantos quase retos, linha fina, sem brilho |
| Ícones | Emoji | Algarismo romano e traço |

O que a p7 faz bem e **fica**:

1. Ordem das 13 dobras e posição dos 3 botões (preço, garantia, FAQ). Sem botão extra.
2. Ritmo: fundo muda a cada dobra, olho nunca cansa.
3. Título sempre com um trecho destacado em cor.
4. Imagem forte logo na primeira tela.
5. Blocos curtos, texto escaneável, uma ideia por dobra.

O que faltou no meu primeiro rascunho (`p6`) e este documento corrige: **peso e contraste**. Papel claro sozinho ficou fraco. A página precisa de dobras escuras intercaladas, título mais grosso e cor de destaque usada com força.

---

## 2. Cores

Tiradas da logo do Acampamento Estoico (oliva e areia), mais um acento quente.

| Nome | Hex | Uso |
|---|---|---|
| Papel | `#F2EAD8` | Fundo claro padrão |
| Papel claro | `#FBF7EE` | Fundo claro alternado, cards sobre papel |
| Areia | `#DCC8A0` | Fundo intermediário, numerais, marca-texto |
| Oliva | `#45452B` | Linhas, rótulos, ícones |
| Noite | `#1F2018` | Fundo escuro, texto principal |
| Terracota | `#B5482A` | Destaque de título e botão. Única cor "que grita" |
| Terracota clara | `#E08A5B` | Destaque de título em fundo Noite |

Regras:

- **Terracota é escassa.** Só aparece em: um trecho por título, botões, preço. Se aparecer em mais lugar, perde força.
- **Não existe preto puro nem branco puro.** Escuro é Noite, claro é Papel.
- **Não existe dourado nem vermelho.** São as cores da p7.
- Texto corrido: Noite sobre claro, Papel sobre escuro. Nunca cinza fraco.

---

## 3. Fontes

| Papel | Fonte | Peso | Observação |
|---|---|---|---|
| Títulos | **Fraunces** | 700–900 | Serifa com corpo. Substitui a Cormorant do rascunho, que ficou fina |
| Destaque no título | Fraunces itálico | 700 | Sempre em terracota |
| Texto | **Figtree** | 400 / 600 | Sans limpa, lê bem em celular |
| Rótulos | Figtree | 700 | CAIXA ALTA, espaçada, 12px. Datas, selos, "Bônus 1" |

Tamanhos no celular:

| Elemento | Tamanho |
|---|---|
| H1 (hero) | 38px |
| H2 (título de dobra) | 30px |
| H3 (título de card) | 21px |
| Texto | 17px |
| Rótulo | 12px |
| Preço | 64px |

Regras:

- Título em **caixa normal**. Caixa alta só em rótulo pequeno.
- H1 é maior que H2. Na p7 os dois têm 24px e a hero perde força.
- Duas famílias, nada mais.

---

## 4. Intercalação das dobras

Três fundos: **claro** (Papel ou Papel claro), **areia**, **escuro** (Noite).
Regra: nunca dois fundos iguais seguidos. Escuro marca virada, prova e autoridade.

| # | Dobra (estrutura p7) | Fundo | Por quê |
|---|---|---|---|
| 1 | Hero | Papel | Entrada clara: já de cara diferente da p7 |
| 2 | Dores ("você repete esse ciclo") | Papel claro | Lista leve, leitura rápida |
| 3 | Erros + virada para o produto | **Noite** | Primeira inversão. Marca o "é por isso que…" |
| 4 | Conteúdo do evento | Papel | Respiro depois do escuro |
| 5 | Bônus | Areia | Tom diferente para separar "extra" do principal |
| 6 | Depoimentos | **Noite** | Prints claros saltam sobre fundo escuro |
| 7 | Preço + **botão 1** | Papel claro | Card de oferta em Noite no centro, botão terracota |
| 8 | Prova social | Papel | |
| 9 | Para quem é / não é | Areia | Duas colunas: sim e não |
| 10 | Sobre o Rafa | **Noite** | Autoridade, foto com luz quente |
| 11 | Garantia + **botão 2** | Papel claro | |
| 12 | Fechamento | **Noite** | Último peso emocional antes do FAQ |
| 13 | FAQ + **botão 3** | Papel | |

Sequência: claro · claro · **escuro** · claro · areia · **escuro** · claro · claro · areia · **escuro** · claro · **escuro** · claro.

Transição entre dobras: corte reto, com filete fino e losango no centro quando duas dobras claras se encostam (1→2 e 7→8).

---

## 5. Destaques

Um recurso por nível. Não acumular.

| Nível | Recurso |
|---|---|
| Trecho-chave do título | Itálico terracota |
| Frase-chave no texto | Marca-texto areia atrás da frase (efeito grifado à mão) |
| Palavra no texto | Negrito, mesma cor |
| Ordem / sequência | Algarismo romano grande em areia (I, II, III) |
| Etiqueta ("Lote 1", "Bônus 2", data) | Rótulo em caixa alta com borda fina oliva |
| Preço | Fraunces 900, 64px, terracota |
| Valor riscado | Oliva, riscado fino |

Proibido: emoji como ícone, brilho/glow, gradiente colorido, sombra difusa, texto todo em caixa alta.

---

## 6. Componentes

- **Botão**: retângulo, raio 6px, fundo terracota, texto Papel claro, Figtree 700 caixa alta. Sem pulsar. Largura total no celular.
- **Card**: fundo Papel claro (ou Noite na oferta), borda 1px oliva translúcida, raio 4px. Sem sombra.
- **Lista de dores/erros**: numeral romano à esquerda, texto à direita, filete entre itens.
- **Filete**: linha fina com losango no centro.
- **Moldura de foto**: arco (topo redondo, base reta), eco do sol da logo.
- **Cronograma**: linha vertical com horários, estilo sumário de livro.
- **FAQ**: sanfona com sinal de + à direita, filete entre perguntas.
- **Textura**: grão de papel sutil em todos os fundos, inclusive o escuro.

Margem lateral no celular: 24px. Espaço vertical de dobra: 64px.

---

## 7. Imagens

- Fotos do Rafa com luz quente, recortadas em arco ou sangrando até a borda.
- Prints de depoimento em resolução alta (mínimo 700px de largura) para não borrar em celular.
- Sem mockup de TV/streaming: é a assinatura da p7.

---

## 8. Em aberto (preciso da sua decisão)

1. **Copy**: uso a de `estoicismo-htm` ("Resgate em 1 dia o estoicismo que os coaches distorceram…") ou a de `Conteudo_Pagina.md` ("Aprenda a manter o controle sobre si…")?
2. **Hero clara ou escura?** Recomendo clara, para diferenciar da p7 na primeira tela. Mas se foi justamente o claro que você achou horrível no rascunho, a hero vira Noite e a página abre escura.
3. **Rascunho `p6`**: apago?
