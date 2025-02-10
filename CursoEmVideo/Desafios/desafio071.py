# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    saque = float(input('Que valor voce quer sacar? R$'))
    print(f'O saque de R${saque} serao necessarios: ')
    nota50 = saque // 50
    saque = saque % 50
    nota20 = saque // 20
    saque = saque % 20
    nota10 = saque // 10
    saque = saque % 10
    nota1 = saque // 1

    print(f'{nota50:.0f} notas de 50')
    print(f'{nota20:.0f} notas de 20')
    print(f'{nota10:.0f} notas de 10')
    print(f'{nota1:.0f} notas de 01')

    escolha = input('Deseja continuar? [S/N]').strip().upper()
    if escolha == 'N':
        break



