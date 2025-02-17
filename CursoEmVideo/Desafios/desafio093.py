"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
partidas = list()
gol = 0
jogador['nome'] = str(input('Nome: '))
totalPartidas = int(input('Partidas jogadas: '))

for contador in range(0, totalPartidas):
    partidas.append(int(input(f'Quantos gols na partida {contador+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
print('-='*20)
for chave, valor in jogador.items():
    print(f'O campo {chave} possui valor {valor}')
print('-='*20)
print(f'O jogodor {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'Na partida {indice+1}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-='*20)

