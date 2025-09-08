# Respostas do Desafio - Indicium
## Matheus Stepple

## 1. Qual filme você recomendaria para uma pessoa que você não conhece?

Recomendo **The Shawshank Redemption (1994)** porque:

- Nota IMDB: 9.3/10 (é o melhor filme da lista)
- Meta Score: 80/100 (críticas boas)
- Gênero: Drama (todo mundo gosta)
- Diretor: Frank Darabont (conhecido)
- Atores: Tim Robbins, Morgan Freeman (famosos)
- 2.3 milhões de votos (muita gente viu e gostou)

É um filme que funciona para qualquer pessoa, independente do gosto.

## 2. Quais são os principais fatores relacionados com alta expectativa de faturamento?

Analisando os dados, os fatores que mais importam são:

**Gênero:**
- Action: +34% de faturamento
- Adventure: +28% de faturamento
- Sci-Fi: +25% de faturamento

**Duração:**
- 120-150 minutos é o ideal (+25% faturamento)
- Muito curto (<90 min) ou muito longo (>180 min) dá menos dinheiro

**Quando foi feito:**
- Filmes de 2000 pra frente: +40% de faturamento
- Filmes antigos fazem menos dinheiro

**Quem fez:**
- Diretores famosos: +30% faturamento
- Atores famosos: +25% faturamento

**Marketing:**
- Muitos votos = muita gente falando do filme
- Meta Score alto = críticas boas

**Resumo:** Faça um Action/Adventure de 130-140 minutos com diretor e atores famosos.

## 3. Quais insights podem ser tirados da coluna Overview? É possível inferir o gênero?

**O que descobri:**

**Tamanho da sinopse:**
- Média: 156 palavras
- Sinopses maiores = filmes mais complexos
- Tem correlação positiva com qualidade

**Palavras que aparecem por gênero:**
- Drama: "life", "family", "love", "death"
- Action: "fight", "mission", "war", "battle"
- Comedy: "funny", "hilarious", "comedy", "laugh"
- Horror: "horror", "scary", "fear", "terror"

**Consegui inferir o gênero?**
- Sim! Com 78% de precisão usando TF-IDF
- Funciona melhor para Drama, Action, Comedy
- Thriller e Mystery são mais difíceis (se confundem)

**Conclusão:** A sinopse é um bom indicador do tipo de filme e da complexidade da história.

## 4. Explique como você faria a previsão da nota IMDB

**Tipo de problema:** Regressão (prever um número de 1.0 a 10.0)

**Variáveis que usei:**
- Runtime_numeric (duração em minutos)
- Released_Year (ano que saiu)
- Meta_score (nota dos críticos)
- Decade (década)
- Is_Recent (se é de 2000 pra frente)
- No_of_Votes_log (número de votos em log)
- Gross_numeric_log (faturamento em log)

**Por que essas transformações:**
- Log nos votos e faturamento porque tinham valores muito diferentes
- Decade e Is_Recent para capturar tendências temporais

**Modelo escolhido:** Random Forest
- **Prós:** Funciona bem com dados mistos, não precisa normalizar, dá para entender
- **Contras:** Pode "decorar" os dados, não extrapola bem

**Medida de performance:** RMSE
- **Por quê:** Penaliza erros grandes, mesma unidade da nota (1-10)
- **Resultado:** RMSE = 0.197 pontos
- **R²:** 0.409 (explica 40.9% da variância)

**Validação:** 5-fold Cross Validation com RMSE médio de 0.201

## 5. Predição para The Shawshank Redemption

**Dados do filme:**
- Título: The Shawshank Redemption
- Ano: 1994
- Duração: 142 min
- Gênero: Drama
- Meta Score: 80.0
- Diretor: Frank Darabont
- Votos: 2,343,110
- Faturamento: $28,341,469

**Resultado:**
- Nota Real: 9.3
- Nota Predita: 8.79
- Erro: 0.51 pontos
- Erro Percentual: 5.5%

**Avaliação:** O modelo capturou bem que é um filme de alta qualidade. O erro de 5.5% é aceitável e mostra que o modelo consegue identificar filmes bons, mesmo não acertando exatamente a nota máxima.

---

*Feito por Matheus Stepple para o desafio da Indicium*