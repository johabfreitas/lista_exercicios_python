'''
6. Usando pandas, leia `notas.csv` e calcule a média de cada aluno a partir das colunas de
notas.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/notas.csv')

colunas_notas = ['Nota1', 'Nota2', 'Nota3']
df['Media_Final'] = df[colunas_notas].mean(axis=1)

print(df)




