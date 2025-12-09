'''
10. Usando pandas, leia `clima.csv` e calcule a temperatura média por cidade.
'''

import pandas as pd

df = pd.read_csv('datasets_exercicios/clima.csv')

temp_media = df.groupby('Cidade')['Temperatura'].mean()

print(df)
print(temp_media)