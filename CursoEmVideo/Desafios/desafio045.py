#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('Suas opcoes: \n[ 0 ] PEDRA\n[ 1 ]PAPEL \n[ 2 ] TESOURA')
jogador = int(input('Qual e sua jogada? '))
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print(f'{'\033[36m'}=-{'\033[m'}'*11)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print(f'{'\033[36m'}=-{'\033[m'}'*11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATS')
    else:
        print('Jogada invalida')
