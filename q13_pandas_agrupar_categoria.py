'''
13. Usando pandas, leia `financeiro.csv`, agrupe por `Categoria` e mostre o gasto total e a
média por categoria.
'''

import pandas as pd

df  = pd.read_csv('datasets_exercicios/financeiro.csv')

gasto_total = df.groupby('Categoria')['Valor'].sum()
media_categoria = df.groupby('Categoria')['Valor'].mean()

print(df)
print()
print(gasto_total)
print()
print(media_categoria)