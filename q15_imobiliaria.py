'''
15. Você trabalha em uma imobiliária e precisa analisar a carteira de imóveis à venda. O
objetivo é entender o preço médio do metro quadrado (m²) por bairro, para ajudar a definir
estratégias de captação e precificação. Seu desafio é:
1.​ Exploração Inicial: Carregue o CSV e veja as informações dos dados e seus registros.
2.​ Engenharia de Features: Crie uma nova coluna no DataFrame chamada Preco_m2,
que será o resultado do Preco_Venda dividido pela Area_m2.
3.​ Análise de Preco_m2: Calcule o preço médio do metro quadrado para cada Bairro.
4.​ Análise por Tipo: Calcule a área média (Area_m2) e o n
'''

import pandas as pd

print('# Passo 1 - Exploração Inicial')
df = pd.read_csv('datasets_exercicios/imoveis.csv')
print(df)
print(50 * '-')

print('# Passo 2 - Engenharia de Features')
df['Preco_m2'] = df['Preco_Venda'] / df['Area_m2']
print(df)
print(50 * '-')

print('# Passo 3 - Análise de Preço')
preco_medio_quadrado = df.groupby('Bairro')['Area_m2'].mean()
print(preco_medio_quadrado)
print(50 * '-')

print('# Passo 4 - Análise por tipo')
print('Área média para cada tipo de imóvel')
area_media = df.groupby('Tipo_Imovel')['Area_m2'].mean()
print(area_media)
print()
print('Quantidade média de quartos')
media_quartos = df.groupby('Tipo_Imovel')['Quartos'].mean()
print(media_quartos)
