#Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um numero: '))

num_ant = numero - 1
num_suc = numero + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(numero, num_ant, num_suc))
                                                        #Tambem funciona: numero, {numero-1}, {numero+1}