#Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#e mostre comprimento da hipotenusa
from math import hypot

oposto = int(input('Digite o cateto oposto do triangulo: '))
adjacente = int(input('Digite o cateto adjacente do triangulo: '))

hipotenusa = hypot(oposto, adjacente)

print(f'O cateto oposto e igual a {oposto}. \nO cateto adjacente e igual a {adjacente} \nE a hipotenusa e igual a {hipotenusa:.2f}')