'''
16. Você é o gerente de logística de uma distribuidora e recebeu um CSV com o balanço do
inventário. Você precisa calcular o estoque final (real) e depois extrair uma amostra
específica para uma auditoria rápida
1.​ Exploração Inicial: Carregue o CSV e rode .info() e .head().
2.​ Engenharia de Features: Crie duas novas colunas - Estoque_Atual: A fórmula é
Estoque_Inicial - Unidades_Vendidas + Unidades_Devolvidas. Valor_Total_Estoque:
A fórmula é o Estoque_Atual (que você acabou de criar) multiplicado pelo
Preco_Custo.
3.​ Análise de Custo: Calcule o valor total em estoque (soma do Valor_Total_Estoque)
para cada Categoria.
4.​ Amostra de Auditoria: A equipe de auditoria pediu uma amostra muito específica.
Use .iloc[] para criar um novo DataFrame df_amostra que contenha:
a.​ Apenas as 3 primeiras linhas (índices 0, 1 e 2).
b.​ Apenas as colunas de índice 1, 3 e 6 (que correspondem a Produto,
Estoque_Inicial e Estoque_Atual).
'''

import pandas as pd

print('# Passo 1 - Exploração Inicial')
df = pd.read_csv('datasets_exercicios/inventario.csv')
print(df)
print(df.info())
print(50 * '-')

print('# Passo 2 - Engenharia de Features')
df['Estoque_Atual'] = (df['Estoque_Inicial'] - df['Unidades_Vendidas'] + df['Unidades_Devolvidas'])
df['Valor_Total_Estoque'] = (df['Estoque_Atual'] * df['Preco_Custo'])
print(df)
print(df.info())
print(50 * '-')

print('# Passo 3 - Análise de Custo')
total_estoque = df.groupby('Categoria')['Valor_Total_Estoque'].sum()
print(total_estoque)
print(50 * '-')

print('# Passo 4: Amostra de Auditoria')
df_amostra = df.iloc[[0,1,2], [1,3,7]]
print(df_amostra)
print(50 * '-')

print("# Reodernando dataframe")
# 1. Obter a lista atual de colunas
colunas = df.columns.tolist()
print(colunas)
# 2. Definir a nova ordem desejada
nova_ordem = ['SKU', 'Produto', 'Categoria', 'Estoque_Inicial', 'Unidades_Vendidas', 'Unidades_Devolvidas', 'Estoque_Atual', 'Preco_Custo', 'Valor_Total_Estoque']
# 3. Reindexar o DataFrame com a nova ordem
df_reordenado = df[nova_ordem]
print("\nDataFrame Reordenado:")
print(df_reordenado.info())

df_amostra = df_reordenado.iloc[[0,1,2], [1,3,6]]
print(df_amostra)