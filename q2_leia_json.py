'''
2. Leia um arquivo JSON chamado `pessoas.json` e exiba o valor da chave `email` de cada
objeto.

O que é?
O comando with open() ler um arquivo JSON
Para que serve?
Para ler arquivo JSON, aqui eu percorro um arquivo JSON com for.
Quando usar?
Quando preciso manipular um arquivo JSON
Exemplo básico
'''

import json

with open('datasets_exercicios/pessoas.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

for dado in dados:
    print(dado['email'])
