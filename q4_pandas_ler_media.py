'''
4. Usando pandas, leia o arquivo `funcionarios.csv` e mostre a idade média dos funcionários.

'''

import pandas as pd

arq = pd.read_csv('datasets_exercicios/funcionarios.csv')

print(arq.head())
print()
print('A média de idade é:', arq['Idade'].mean())
