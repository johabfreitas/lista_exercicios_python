'''
18. Você é um cientista de dados monitorando a qualidade do ar em diferentes zonas de uma
cidade. Você recebeu um CSV (sensores_qualidade.csv) que registra as leituras de material
particulado (PM2.5) de hora em hora, coletadas por vários sensores. O problema é que osdados vieram em um formato "largo" (wide), onde cada hora é uma coluna. Você precisa
processar esses dados para calcular médias, identificar picos de poluição e classificar o status
de cada sensor. Seu desafio é:
1.​ Exploração Inicial: Carregue o CSV, rode .info() e .head().
2.​ Processamento com iloc e for: As leituras estão nas colunas de índice 3 a 8
(Leitura_H1 a Leitura_H6). Crie duas novas colunas (Media_PM25 e Pico_PM25).
Você deve usar um loop para iterar pelas linhas:
a.​ Em cada linha, use .iloc para selecionar apenas as 6 colunas de leitura daquela
linha.
b.​ Calcule a média dessas leituras e armazene na lista para a coluna
Media_PM25.
c.​ Calcule o valor máximo (pico) dessas leituras e armazene na lista para a
coluna Pico_PM25.
3.​ Classificação Condicional: Adicione uma lógica condicional para criar uma terceira
coluna, Nivel_Alerta:
a.​ Primeiro, verifique o Status_Operacional (coluna de índice 2). Se for
"Inativo", o Nivel_Alerta deve ser "Offline".
b.​ Se o Pico_PM25 (que você calculou) for maior que 25.0, o Nivel_Alerta deve
ser "Perigoso".
c.​ Se a Media_PM25 (que você calculou) for maior que 15.0, o Nivel_Alerta
deve ser "Alerta".
d.​ Caso contrário, o Nivel_Alerta deve ser "Normal".
4.​ Análise Estatística: Calcule e exiba a média da Media_PM25 e a média do
Pico_PM25 para cada Localizacao (Centro, Zona Norte, Zona Sul).
'''

import pandas as pd

# 1. Exploração Inicial
# Carregamos o arquivo CSV
df = pd.read_csv('datasets_exercicios/sensor_qualidade.csv')

# Exibindo informações e as primeiras linhas
print("--- Informações do DataFrame ---")
df.info()
print("\n--- Primeiras Linhas ---")
print(df.head())

# Preparando listas para armazenar os resultados
medias = []
picos = []
alertas = []

# 2. Processamento com iloc e for
# Iteramos pelo índice de cada linha do DataFrame
for i in range(len(df)):

    # a. Seleção com iloc: linhas 'i', colunas 3 até 8 (índice 9 é exclusivo)
    leituras_linha = df.iloc[i, 3:9]

    # b. Cálculo da média
    media_val = leituras_linha.mean()
    medias.append(media_val)

    # c. Cálculo do pico (máximo)
    pico_val = leituras_linha.max()
    picos.append(pico_val)

    # 3. Classificação Condicional
    status_op = df.iloc[i, 2]  # Coluna de índice 2 é Status_Operacional

    # Lógica sequencial conforme prioridade
    if status_op == 'Inativo':
        alertas.append('Offline')
    elif pico_val > 25.0:
        alertas.append('Perigoso')
    elif media_val > 15.0:
        alertas.append('Alerta')
    else:
        alertas.append('Normal')

# Atribuindo as listas calculadas às novas colunas
df['Media_PM25'] = medias
df['Pico_PM25'] = picos
df['Nivel_Alerta'] = alertas

# Exibindo resultado intermediário para verificação
print("\n--- Dados Processados (Amostra) ---")
print(df[['Localizacao', 'Media_PM25', 'Pico_PM25', 'Nivel_Alerta']].head())

# 4. Análise Estatística
# Agrupando por localização e calculando as médias solicitadas
print("\n--- Estatísticas por Localização ---")
stats_loc = df.groupby('Localizacao')[['Media_PM25', 'Pico_PM25']].mean()
print(stats_loc)