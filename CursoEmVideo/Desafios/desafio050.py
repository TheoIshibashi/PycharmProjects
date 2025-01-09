#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        s = s + numero
        cont = cont + 1
print(f'voce informou {cont} numeros pares e a soma foi {s}')
