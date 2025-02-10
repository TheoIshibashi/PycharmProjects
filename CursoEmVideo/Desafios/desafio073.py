#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Vasco.

tabela_brasileirao_2024 = (
    'Botafogo',
    'Palmeiras',
    'Flamengo',
    'Fortaleza',
    'Internacional',
    'Grêmio',
    'Fluminense',
    'São Paulo',
    'Cruzeiro',
    'Corinthians',
    'Athletico-PR',
    'Red Bull Bragantino',
    'Bahia',
    'Cuiabá',
    'Vasco',
    'Santos',
    'Goiás',
    'América-MG',
    'Coritiba',
    'Atlético-MG'
)

print('-='*15)
print(f'Lista dos times do Brasileirao: {tabela_brasileirao_2024}')
print('-='*15)
#a) Os 5 primeiros times.
print('A) Os primeiros 5 times da tabela.')
for cont in range(0,5):
    print(f'{cont+1} Colocado: {tabela_brasileirao_2024[cont]}')

#b) Os últimos 4 colocados.
print('-='*15)
print('b) Os últimos 4 colocados.')
for contB in range(len(tabela_brasileirao_2024) - 4, len(tabela_brasileirao_2024)):
    print(f'{contB+1} Colocado: {tabela_brasileirao_2024[contB]}')

#c) Times em ordem alfabética.
print('-='*15)
print('c) Times em ordem alfabética.')
ordem = sorted(tabela_brasileirao_2024)
for contC, time in enumerate(ordem):
    print(f'Posicao {contC+1}: {time}')

#d) Em que posição está o time da Vasco.
print('-='*15)
print('d) Em que posição está o time do Vasco.')
for contD, vasco in enumerate(tabela_brasileirao_2024):
    if vasco in 'Vasco':
        print(f'O {vasco} se encontra na posicao {contD+1} do brasileirao.')
print('-='*15)

"""
print('a) Os 5 primeiros times.')
for cont in range(0, 5):
    print(f'{cont+1} Colocado: {tabela_brasileirao_2024[cont]}')

print('=-'*15)
print('b) Os últimos 4 colocados.')
for contB in range(len(tabela_brasileirao_2024) - 4, len(tabela_brasileirao_2024)):
    print(f'{contB+1} Colocado: {tabela_brasileirao_2024[contB]}')

print('=-'*15)
print('c) Times em ordem alfabética.')
times_ordenados = sorted(tabela_brasileirao_2024)
for contC, time in enumerate(times_ordenados, start=1):
    print(f'{contC} {time}')

print('=-'*15)
print('d) Em que posição está o time do Vasco.')
for contD, vasco in enumerate(tabela_brasileirao_2024):
    if vasco == 'Vasco':
        print(f'{contD} Posicao: {vasco}')

print('a) Os 5 primeiros times.')
for cont in range(0, 5):
    print(f'{cont+1} Colocado: {tabela_brasileirao_2024[cont]}')

print('=-'*15)
print('b) Os últimos 4 colocados.')
for contB in range(len(tabela_brasileirao_2024) - 4, len(tabela_brasileirao_2024)):
    print(f'{contB+1} Colocado: {tabela_brasileirao_2024[contB]}')

print('=-'*15)
print('c) Times em ordem alfabética.')
times_ordenados = sorted(tabela_brasileirao_2024)
for contC, time in enumerate(times_ordenados, start=1):
    print(f'{contC} {time}')

print('=-'*15)
print('d) Em que posição está o time do Vasco.')
for contD, vasco in enumerate(tabela_brasileirao_2024):
    if vasco == 'Vasco':
        print(f'{contD} Posicao: {vasco}')
"""
