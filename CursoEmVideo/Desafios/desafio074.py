#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
from random import randint

maior = 0
menor = 0

#Simples:
numeros = randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)

#Versao com for, append e transformando a lista em tupla
"""for i in range(0, 5):
    numeros.append(random.randint(1, 100))
numeros = tuple(numeros)"""

ordem = sorted(numeros, reverse=True)
print('Numeros gerados:',end=' ')
for i in range(len(numeros)):
    print(f'{numeros[i]}', end=', ')
print(f'\nb)Maior valor: {max(ordem)}')
print(f'c)Menor valor: {min(ordem)}')
