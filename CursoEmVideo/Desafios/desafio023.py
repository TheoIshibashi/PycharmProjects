# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Caso coloque um numero menor que milhar, este nao programa funcionara

numero = input('Digite um numero de 0 a 9999: ')
numero.replace("", " ")
numero.split()
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')