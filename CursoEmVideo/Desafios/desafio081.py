"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
escolha = ''
numero = int(input('Digite um numero: '))
cinco = False
lista.append(numero)
while True:
    escolha = input('Deseja continuar? [S/N]:')
    if escolha.upper() == 'S':
        numero = int(input('Digite um numero: '))
        lista.append(numero)
    else:
        break

print(f'A)Foram digitados {len(lista)} elementos')
print(f'B) A lista de valores ordenada de forma decrescente. {sorted(lista)}')
if 5 in lista:
    print('O numero 5 foi digitado e esta na lista nas posicoes: ', end='')
else:
    print('O numero 5 nao foi digitado e nao esta na lista.')

for cont, valor in enumerate(lista):
    if valor == 5:
        print(f'{cont}', end=' ')





