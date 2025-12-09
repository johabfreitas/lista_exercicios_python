'''
19. Você é analista de dados em uma empresa e recebeu um CSV (desempenho_vendas.csv)
com o desempenho trimestral (Q1, Q2, Q3, Q4) da equipe de vendas. Você precisa calcular o
total vendido no ano, a média, e criar uma nova categoria de comissão baseada em regras.
Além disso, a diretoria pediu um relatório amostral dos piores e melhores vendedores, o que
exigirá o uso de iloc. Seu desafio é:
1.​ Engenharia de Features (Estatística):
a.​ Crie uma coluna Total_Vendido somando as 4 colunas de vendas (Vendas_Q1
a Vendas_Q4).
b.​ Crie uma coluna Atingiu_Meta que seja True se Total_Vendido >=
Meta_Anual, e False caso contrário.
2.​ Processamento de regras de bonus: Crie uma nova coluna Bonus_Especial. Use um
loop for para iterar pelas linhas:
a.​ Regra 1: Se o vendedor não atingiu a meta (Atingiu_Meta == False), o
Bonus_Especial é 0.
b.​ Regra 2: Se o vendedor atingiu a meta, ele ganha um bônus base de R$ 1.000.c.​ Regra 3: Se ele atingiu a meta (Regra 2), verifique também se ele teve
"Crescimento Consistente". Um vendedor teve crescimento consistente se
Vendas_Q4 > Vendas_Q3 > Vendas_Q2 > Vendas_Q1. Se teve, adicione R$
2.000 ao bônus (totalizando R$ 3.000).
3.​ Análise Estatística: Calcule o Total Vendido (soma) e a taxa de atingimento de meta
(média) por Equipe. (Dica: A média de uma coluna booleana (True/False) retorna a
taxa/percentual de True).
4.​ Relatório:
a.​ Ordene o DataFrame pelo Total_Vendido (do menor para o maior).
b.​ Exibir um "Relatório de Extremos" que contenha apenas os 2 piores
vendedores (as 2 primeiras linhas) e os 2 melhores vendedores (as 2 últimas
linhas).
'''

import pandas as pd

# --- 0. Criando o Dataset simulado (Para você poder rodar o código) ---
'''
data = {
    'Vendedor': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena'],
    'Equipe': ['Alpha', 'Beta', 'Alpha', 'Gamma', 'Beta', 'Alpha', 'Gamma', 'Beta'],
    'Meta_Anual': [50000, 60000, 55000, 50000, 70000, 45000, 60000, 55000],
    'Vendas_Q1': [10000, 12000, 15000, 10000, 15000, 8000, 14000, 13000],
    'Vendas_Q2': [12000, 11000, 14000, 12000, 16000, 10000, 15000, 14000],
    'Vendas_Q3': [14000, 18000, 13000, 15000, 18000, 12000, 16000, 15000],
    'Vendas_Q4': [15000, 15000, 12000, 18000, 25000, 16000, 17000, 16000]
}
'''
df = pd.read_csv('datasets_exercicios/desempenho_vandas.csv')

print("--- DataFrame Original ---")
print(df.head())
print("-" * 50)

# --- 1. Engenharia de Features (Estatística) ---
# a. Coluna Total_Vendido (Soma das colunas)
df['Total_Vendido'] = df['Vendas_Q1'] + df['Vendas_Q2'] + df['Vendas_Q3'] + df['Vendas_Q4']

# b. Coluna Atingiu_Meta (Booleana)
df['Atingiu_Meta'] = df['Total_Vendido'] >= df['Meta_Anual']

# --- 2. Processamento de regras de bônus (Loop for) ---
lista_bonus = []

for i in range(len(df)):
    # Capturando dados da linha atual para facilitar a leitura da lógica
    atingiu = df.loc[i, 'Atingiu_Meta']
    q1 = df.loc[i, 'Vendas_Q1']
    q2 = df.loc[i, 'Vendas_Q2']
    q3 = df.loc[i, 'Vendas_Q3']
    q4 = df.loc[i, 'Vendas_Q4']

    # Regra 1: Não atingiu meta -> 0
    if not atingiu:
        bonus = 0
    else:
        # Regra 2: Atingiu meta -> Base 1000
        bonus = 1000

        # Regra 3: Checagem de Crescimento Consistente (Q4 > Q3 > Q2 > Q1)
        if (q4 > q3) and (q3 > q2) and (q2 > q1):
            bonus += 2000  # Adiciona 2000, totalizando 3000

    lista_bonus.append(bonus)

df['Bonus_Especial'] = lista_bonus

# --- 3. Análise Estatística por Equipe ---
# Agrupamos por Equipe
analise_equipe = df.groupby('Equipe').agg({
    'Total_Vendido': 'sum',  # Soma total de vendas
    'Atingiu_Meta': 'mean'  # Média de True/False dá a porcentagem de acerto (ex: 0.66 = 66%)
}).reset_index()

# Renomeando colunas para ficar mais bonito
analise_equipe.columns = ['Equipe', 'Soma_Vendas', 'Taxa_Meta_Atingida']

print("\n--- Análise por Equipe ---")
print(analise_equipe)
print("-" * 50)

# --- 4. Relatório de Extremos (iloc) ---
# a. Ordenar pelo Total_Vendido
df_ordenado = df.sort_values(by='Total_Vendido', ascending=True)

# b. Selecionar os 2 piores (início) e os 2 melhores (fim)
piores_vendedores = df_ordenado.iloc[:2]
melhores_vendedores = df_ordenado.iloc[-2:]

# Concatenando para criar um único relatório
relatorio_extremos = pd.concat([piores_vendedores, melhores_vendedores])

print("\n--- Relatório de Extremos (2 Piores e 2 Melhores) ---")
print(relatorio_extremos[['Vendedor', 'Equipe', 'Total_Vendido', 'Atingiu_Meta', 'Bonus_Especial']])