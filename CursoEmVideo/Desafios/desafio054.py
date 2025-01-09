#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
menor = 0
maior = 0

for i in range(0, 7):
    ano = int(input('Digite sua data de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'O numero de pessoas que ainda não atingiram a maior idade é igual a: {menor}')
print('O numero de pessoas que ja atingiram a maior idade é igual a: {}'.format(maior))