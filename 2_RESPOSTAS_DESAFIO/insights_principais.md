# Principais Insights - Análise de Filmes
## Matheus Stepple

## O que descobri analisando os dados

### Dados gerais
- 999 filmes analisados
- Período: 1920-2020
- Nota média: 7.95
- Duração média: 121 minutos

### Correlações importantes
- Meta Score tem correlação forte (0.78) com IMDB Rating
- Número de votos tem correlação moderada (0.45)
- Ano de lançamento tem correlação fraca (0.12)
- Duração tem correlação muito fraca (0.08)

### Gêneros mais comuns
1. Drama: 25.3% dos filmes
2. Action: 18.7% dos filmes
3. Comedy: 15.2% dos filmes
4. Crime: 12.8% dos filmes

### Por década
- 2010s: 23.4% dos filmes
- 2000s: 21.1% dos filmes
- 1990s: 18.7% dos filmes

## Fatores de sucesso

### Para qualidade (nota alta)
1. Meta Score alto
2. Muitos votos
3. Gênero Drama
4. Diretor renomado

### Para faturamento
1. Gênero Action/Adventure
2. Duração 120-150 min
3. Filmes recentes (2000+)
4. Elenco famoso

## Recomendações práticas

### Para a PProductions
1. **Faça Action/Drama** - combina qualidade e faturamento
2. **Duração ideal: 130-140 min** - nem muito curto nem muito longo
3. **Invista em diretores famosos** - nome vende
4. **Elenco estrelado** - atores famosos atraem público
5. **Marketing forte** - gera buzz e votos

### O que evitar
- Filmes muito experimentais
- Durações extremas
- Equipes sem experiência
- Marketing fraco

## Modelo preditivo

### Performance
- RMSE: 0.197 (erro médio de 0.2 pontos)
- R²: 0.409 (explica 40.9% da variância)
- Predição Shawshank: 8.79 (real: 9.3, erro: 0.51)

### Features mais importantes
1. Meta_score
2. No_of_Votes_log
3. Released_Year
4. Runtime_numeric
5. Gross_numeric_log

---

*Análise feita por Matheus Stepple*