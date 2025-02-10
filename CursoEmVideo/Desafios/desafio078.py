"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
from operator import index

valores = []
maior = 0
posicao_maior = 0
menor = -1
posicao_menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Voce digitou os seguintes valores: {valores}')
print(f'O maior valor da digitado foi {maior} nas posicoes: ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}, ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes: ', end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}, ', end='')
print()


