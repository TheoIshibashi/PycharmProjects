"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais"""

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
else:
    print('AMBOS os valores são iguais')