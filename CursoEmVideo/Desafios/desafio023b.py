# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Caso coloque um numero menor que milhar, este programa funcionara
numero = int(input('Digite um numero de 0 a 9999: '))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')