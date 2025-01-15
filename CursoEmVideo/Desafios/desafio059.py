"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

resultado = 0
opcao = 0
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

while opcao != 5:
    print('MENU\n[ 1 ] somar\n[ 2 ] multiplica \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    escolha = int(input('Qual opcao voce deseja? '))
    if escolha == 1:
        resultado = numero1 + numero2
        print('A soma entre {} + {} vale: {}'.format(numero1, numero2, resultado))

    elif escolha == 2:
        resultado = numero1 * numero2
        print('A multiplicacao entre {} x {} vale: {}'.format(numero1, numero2, resultado))

    elif escolha == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'Entre {numero1} e {numero2} o maior vale é {maior}')

    elif escolha == 4:
        print('Insira novos valores: ')
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))

    elif escolha == 5:
        print('Finalizando...')
        break
    else:
        print('Opcao invalida')

