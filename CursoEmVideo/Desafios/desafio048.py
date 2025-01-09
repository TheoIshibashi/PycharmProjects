#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
import time

s = 0
cont = 0
print('Calculando resultado de 500 numeros...')
time.sleep(3)

for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        s = s + num
print(f'A soma de todos os {cont} valores solicitados é: {s}')
