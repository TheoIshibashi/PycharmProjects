"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""


time = list()


while True:
    jogador = dict()
    partidas = list()

    jogador['nome'] = str(input('Nome: '))
    totalPartidas = int(input('Partidas jogadas: '))

    for contador in range(0, totalPartidas):
        partidas.append(int(input(f'Quantos gols na partida {contador+1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
        print('ERRO! Responda com apenas S ou N')

    if opcao == 'N':
        break

# Exibir os resultados formatados
print('-' * 45)
print(f"{'ID':<4}{'Nome':<15}{'Gols':<20}{'Total'}")
print('-' * 45)

for chave, valor in enumerate(time):
    print(f"{chave:<4}{valor['nome']:<15}{str(valor['gols']):<20}{valor['total']}")

print('-' * 45)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]} -- ')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'No jogo {indice+1} fez {gols} gols.')
    print('-'*45)
print(f'<<< VOLTE SEMPRE >>>')









"""
for atleta in time:
    for chave, valor in atleta.items():
        print(f'{chave}: {valor}', end=' ')
    print()


while True:
    dadosJogador = str(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dadosJogador == 999:
        break
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {jogador['nome']}')
"""