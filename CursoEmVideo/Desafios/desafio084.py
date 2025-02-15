"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

leve = pesado = 0
pessoas = list()
dados = list()

cadastros = 0

opcao = 'S'
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])

    cadastros += 1
    dados.clear()

    opcao = input('Deseja continuar? [S/N] ')
    if opcao in 'nN':
        break
print('=-'*20)
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas...')

#Vericica o maior peso e quem eh
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]}', end='')
print()

#Verifica o menor peso e quem eh
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]}', end='')
print()
print('=-'*20)







