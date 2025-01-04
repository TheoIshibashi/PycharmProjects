#Crie um programa que leia um numero real qualquer pelo teclado e mostre na teal a sua porcao inteira
from math import trunc

real_num = float(input('Digite um numero real: '))
full_num = trunc(real_num)
print(f'A porcao inteira de {real_num:.3f} e igual a {full_num}')
