# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import  randint
contador = 0
print('=-'*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*25)
while True:
    numero = int(input('Diga um valor: '))
    escolha = input('Você deseja par ou impar? [P/I] ').upper().strip()
    computador = randint(0, 10)
    print('--' * 25)
    soma = numero + computador
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Voce jogou {numero} e o computador escolheu {computador}. Total de {soma} DEU PAR')
            print('Voce acertou! Jogue novamente!')
            print('--' * 25)
            contador += 1
        else:
            print(f'Voce jogou {numero} e o computador escolheu {computador}. Total de {soma} DEU IMPAR')
            print('--' * 25)
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print(f'Voce jogou {numero} e o computador escolheu {computador}. Total de {soma} DEU IMPAR')
            print('Voce acertou! Jogue novamente!')
            print('--'*25)
            contador += 1
        else:
            print(f'Voce jogou {numero} e o computador escolheu {computador}. Total de {soma} DEU PAR')
            print('--' * 25)
            break
print(f'GAME OVER! Voce venceu {contador} vezes concecutivas.')
