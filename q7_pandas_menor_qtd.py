'''
7. Usando pandas, leia `estoque.csv` e mostre apenas os produtos com quantidade menor que
10.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/estoque.csv')

# produtos_menor_10 = df[df['Quantidade'] < 10] # forma feia
produtos_menor_10 = df.query('Quantidade < 10') # forma elegante

print(produtos_menor_10)

