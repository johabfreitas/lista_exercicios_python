'''
14. Você é analista de dados em uma plataforma que vende produtos digitais (cursos, ebooks,
software). Você recebeu um CSV com as vendas dos últimos dias e precisa gerar um relatório
sobre o faturamento e a popularidade dos produto. Seu desafio é:
1.​ Exploração Inicial: Carregue o CSV e veja as informações dos dados e seus registros.
2.​ Estatísticas Gerais de Vendas: Calcule e exiba:
3.​ O Faturamento Total (soma de todos os Preco_Unitario).
4.​ O Ticket Médio (preço médio de todas as vendas).
5.​ Faturamento por Categoria: Calcule o faturamento total para cada Categoria de
produto (Curso Online, Ebook, etc.).
6.​ Popularidade do Pagamento: descobrir qual o método de pagamento mais utilizado.
'''
from itertools import count

import pandas as pd

print('# Passo 1 - exploração inicial')
df  = pd.read_csv('datasets_exercicios/venda_digital.csv')
print(df)
print(50*'-')

print('# Passo 2  - estatísticas de vendas')
print(df.describe())
print(50*'-')

print('# Passo 3 - faturamento total')
faturamento_total = df['Preco_Unitario'].sum()
print(f'O faturamento das vendas foi de R${faturamento_total:.2f}')
print(50*'-')

print('# Passo 4 - preço médio de vendas')
preco_medio = df['Preco_Unitario'].mean()
print(f'O preço médio foi de R${preco_medio:.2f}')
print(50*'-')

print('# Passo 5 - Faturamento')
faturamento_categoria = df.groupby('Categoria')['Preco_Unitario'].sum()
print(faturamento_categoria)
print(50*'-')

print('# Passo 6 - Popularidade do Pagamento')
metodo_pgto_mais_utilizado = df['Metodo_Pagamento'].value_counts()
print(metodo_pgto_mais_utilizado)
