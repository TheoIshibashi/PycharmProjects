#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
menor = num1
maior = num1
if num1<num2 and num1<num3:
    menor = num1
if num2<num3 and num2<num1:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

if num1>num2 and num1>num3:
    maior = num1
if num2>num3 and num2>num1:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

print(f'Primeiro valor: {num1} \nSegundo valor: {num2} \nTerceiro valor: {num3}')
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
