#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input('Digite um numero para calcular seu fatorial: '))
c = numero
f = 1
print('Calculando...')
print(f'{c}! -> ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))