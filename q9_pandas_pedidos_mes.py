'''
9. Usando pandas, leia `pedidos.csv` e mostre apenas os pedidos feitos no mês de janeiro.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/pedidos.csv')

filtrar_janeiro = df[df['Data'] < '2024-02-10']

print(df)
print()
print(filtrar_janeiro)