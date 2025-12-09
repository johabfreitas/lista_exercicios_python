'''
17. O time de Marketing precisa de uma lista de clientes para uma campanha de e-mail. Eles
precisam formatar os nomes e calcular o ticket médio. Além disso, eles notaram que as
últimas linhas do CSV de exportação são dados "sujos" do sistema e precisam ser removidos.
Seu desafio é:
1.​ Exploração Inicial: Carregue o CSV marketing.csv para ver os dados sujos no final.
2.​ Limpeza de Dados: Os dados exportados sempre incluem 2 linhas "sujas" de
metadados no final. Use .iloc[] para criar um novo DataFrame df_limpo que contenha
todas as linhas, exceto as duas últimas.
3.​ Engenharia de Features: No df_limpo, crie duas novas colunas:
a.​ Nome_Completo: O resultado da concatenação (junção) das colunas Nome e
Sobrenome, separadas por um espaço.
b.​ Ticket_Medio: O resultado da divisão de Total_Gasto por Total_Pedidos.
c.​ Análise de Risco: Alguns clientes têm Total_Pedidos igual a 0 (o que causaria
um erro de divisão por zero). Antes de calcular o Ticket_Medio, substitua os
zeros da coluna Total_Pedidos por 1 (use replace ou .loc[]).
d.​ Análise Estatística: Calcule o Ticket Médio (Ticket_Medio) geral da base de
clientes limpa.
'''

import pandas as pd

print('# Passo 1: Exploração Inicial')
df = pd.read_csv('datasets_exercicios/marketing.csv')
print(df)
print(df.info())
print(50 * '-')

print('# Passo 2: Limpeza de Dados')
df_limpo = df.iloc[0:6]
print(df_limpo)
print(50 * '-')

print('# Passo3: Engenharia de Features')
df_limpo.loc[:, 'Nome_Completo'] = df_limpo['Nome'] + ' ' + df_limpo['Sobrenome']
print(df_limpo)

df_limpo['Ticket_Medio'] = df_limpo['Total_Gasto'] / df_limpo['Total_Pedidos']
print(df_limpo)

df_limpo['Total_Pedidos'] = df_limpo['Total_Pedidos'].replace(3, 1)
valor_ticket_medio = df_limpo['Ticket_Medio'].mean()
print(f'O valor médio do ticket é R${valor_ticket_medio:.2f}')