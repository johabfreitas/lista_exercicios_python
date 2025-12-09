'''
11. Usando pandas, leia `transacoes.csv` e mostre o valor total gasto por cada cliente.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/transacoes.csv')

total_gasto_cliente = df.groupby('Cliente')['Valor'].sum()

print(df.head())
print(total_gasto_cliente)