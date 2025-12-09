'''
12. Usando pandas, leia `alunos.csv` e reorganize as colunas para exibir apenas `Nome`,
`Curso` e a média das notas.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/alunos.csv')

colunas_notas = ['Nota1', 'Nota2', 'Nota3']
df['Media_Final'] = df[colunas_notas].mean(axis=1)

novo_df = df[['Nome', 'Curso', 'Media_Final']]
print(novo_df)
