'''
8. Usando pandas, leia `filmes.csv` e exiba a contagem de filmes por gênero.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/filmes.csv')

contagem_genero = df['Genero'].value_counts()

print()
print(df)
print(contagem_genero)