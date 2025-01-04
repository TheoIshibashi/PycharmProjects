#Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import cos, sin, tan, radians

angulo = float(input('Digite um angulo qualquer: '))
angulo_radiano = radians(angulo)

cosseno = cos(angulo_radiano)
seno = sin(angulo_radiano)
tangente = tan(angulo_radiano)

print(f'Cosseno: {cosseno:.2f} \nSeno: {seno:.2f} \nTangente: {tangente:.2f}')