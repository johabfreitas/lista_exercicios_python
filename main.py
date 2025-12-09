'''
Script para teste.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/venda_digital.csv')

print(df.iloc[0]['Preco_Unitario'].sum()/2)
print(df.iloc[0:2,1])
print(df.iloc[1:3,0:3])