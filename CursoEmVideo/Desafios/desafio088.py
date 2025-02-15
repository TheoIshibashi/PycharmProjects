"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint

lista = list()
jogos = list()
print('='*20)
print('     JOGA NA MEGA SENA    ')
print('='*20)
quantidadeJogos = int(input('Quantass jogos voce quer que eu sorteie? '))
total = 1
while total <= quantidadeJogos:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'SORTEANDO {quantidadeJogos} JOGOS', '-=' * 3)

for indice, list in enumerate(jogos):
    print(f'Jogo {indice+1}: {list}')