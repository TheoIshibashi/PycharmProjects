"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

cores = {
'limpa': '\033[m',
'ciano': '\033[36m',
'verde': '\033[32m',
'vermelho': '\033[31m'
}
computador = randint(0,5)
print(f'{cores['ciano']}-=-{cores['limpa']}' * 20)
print(f'Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print(f'{cores['ciano']}-=-{cores['limpa']}' * 20)
choice = int(input('Em que numero eu pensei? '))

print(f'{cores['vermelho']}PROCESSANDO...{cores['limpa']}')
sleep(3)

if choice == computador:
    print(f'{cores['verde']}PARABENS!!! Voce conseguiu me vencer! {cores['limpa']}')
else:
    print(f'{cores['vermelho']}GANHEI!!! Eu pensei no {computador} e nao no {choice}{cores['limpa']}')
