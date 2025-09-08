# Desafio Indicium - Análise de Filmes
## Matheus Stepple

Fiz uma análise de dados de filmes para ajudar a PProductions a decidir que tipo de filme fazer.

## O que tem aqui

```
LH_CD_MATHEUS_STEPPLE/
├── README.md
├── requirements.txt
├── desafio_indicium_imdb.csv
├── 1_ANALISE_EXPLORATORIA/
│   └── analise_exploratoria.ipynb
├── 2_RESPOSTAS_DESAFIO/
│   ├── respostas_desafio.md
│   └── insights_principais.md
├── 3_MODELO_PREDITIVO/
│   ├── modelo_preditivo.ipynb
│   └── modelo.py
├── 4_RELATORIO/
│   └── relatorio_desafio_indicium.pdf
└── 5_CODIGO_FONTE/
    └── analise_completa.py
    
```

## Como rodar

1. Instalar as coisas:
```bash
pip install -r requirements.txt
```

2. Ver a análise:
```bash
jupyter notebook 1_ANALISE_EXPLORATORIA/analise_exploratoria.ipynb
```

3. Treinar o modelo:
```bash
jupyter notebook 3_MODELO_PREDITIVO/modelo_preditivo.ipynb
```

4. Criar o modelo:
```bash
python 3_MODELO_PREDITIVO/modelo.py
```

## O que descobri

- 999 filmes analisados
- Nota média: 7.95
- Usei Random Forest
- RMSE: 0.197, R²: 0.409
- The Shawshank Redemption: predição 8.79 (real: 9.3)

##O que usei

- Python
- pandas, numpy
- scikit-learn
- matplotlib
- Random Forest

## Contato

Matheus Stepple
- Email: matheusstepplegomes@gmail.com OU msg2@cin.ufpe.br
- LinkedIn: https://www.linkedin.com/in/matheus-stepple/


Feito para o processo da Indicium
