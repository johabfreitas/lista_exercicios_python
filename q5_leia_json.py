'''
5. Leia um arquivo JSON chamado `livros.json` e exiba apenas os títulos dos livros com mais
de 300 páginas.
'''

import json as js

with open('datasets_exercicios/livros.json', 'r', encoding='utf-8') as arquivo:
    dados = js.load(arquivo)

print(dados)

for dado in dados:
    if dado['paginas'] > 300:
        print(dado['titulo'])


