#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero: '))
resto = numero % 2
if resto == 0:
    print(f'{numero} e Par!')
else:
    print(f'{numero} e Impar!')