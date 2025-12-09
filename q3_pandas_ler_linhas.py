'''
3. Usando pandas, leia o arquivo `vendas.csv` e exiba apenas as primeiras 3 linhas.
O que é?
    Pandas é uma biblioteca para manipulação e análise de dados.
Pra que serve?
    O Pandas permite que realize limpeza, tratamento e transformações em dados.
Quando usar?
    Sempre que precisar manipular, limpar, analisar e organizar dados em formato de tabela.
Exemplo
'''

import pandas as pd

arq = pd.read_csv('datasets_exercicios/vendas.csv')

print(arq.head(3))


