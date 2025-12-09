'''
1. Leia um arquivo CSV chamado `produtos.csv` e exiba cada linha como lista usando o
módulo `csv`

O que é?
with open() é um comando em Python
Para que serve?
Ele faz a leitura e escrita de um arquivo, fechando o arquivo automaticamente.
Quando usar?
Quando tem a necessidade de ler e escrever um arquivo.

Exemplo Básico
'''

import csv

with open('datasets_exercicios/produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
