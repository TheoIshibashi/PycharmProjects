#Faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um numero: '))

for i in range (1,11):

    r = i*numero

    print("{} x {} = {}".format(numero, i, r))

    i = i+1
