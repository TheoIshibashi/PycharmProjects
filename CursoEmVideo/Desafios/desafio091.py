"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from operator import itemgetter
maior = 0
jogadas = dict()
lista = list()
ordem = list()
for contador in range(0,4):
    jogadas['Jogador'] = contador+1
    jogadas['Dado'] = randint(1, 6)
    if jogadas['Dado'] > maior:
        maior = jogadas['Dado']
    lista.append(jogadas.copy())

    ordem = sorted(lista, key=itemgetter('Dado'), reverse=True)
for jogadas in lista:
    for chave, valor in jogadas.items():
        print(f'{chave} {valor}', end=' ')
    print()

print('\nRanking de jogadores:')
for jogadas in ordem:
    for chave, valor in jogadas.items():
        print(f'{chave} {valor}', end=' ')
    print()

for jogadas in ordem:
    for chave, valor in jogadas.items():
        if valor == maior:
            print(f'O jogador {jogadas['Jogador']} foi o vencedor por ter tirado {valor} no dado')

