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

