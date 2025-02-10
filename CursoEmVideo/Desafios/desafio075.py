#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#simples
numeros = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')),
       int(input('Digite o primeiro valor: ')))

print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3)+1} posicao')
print('Os valores pares foram ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=', ')

#complicado
"""for i in range(0, 4):
    #Input dos numeros e adiciona eles na tupla
    numero = int(input('Digite um numero:'))
    numeros.append(numero)
    #Verifica se o numero digitado e par, se sim adiciona ele a outra tupla pares.
    if numero % 2 == 0:
        pares.append(numero)
    #Verifica quantas vezes aparece o numero 9
    if 9 in numeros:
        cont_nove = cont_nove + 1
    #Verifica se existe o numero 3 e caso tenha mostra a posicao do primeiro 3 da tupla.
    if 3 in numeros:
        pos_tres = numeros.index(3)

print(f'A)O nove apareceu {cont_nove} vezes')
print(f'B)O primeiro numero tres da tupla esta na posicao: {pos_tres+1}')
print(f'C) Os numero pares sao: {pares}')"""





















"""numeros = []
contador_nove = 0
pos_tres = 0
pares = []
for i in range(0, 5):
    num = int(input('Digite um numero: '))
    numeros.append(num)
    if int(num) % 2 == 0:
        pares.append(num)
    if num == 9:
        contador_nove += 1
#Verifica a posicao do primeiro 3 com o metodo index, que retorna o primeiro valor especificado.
if 3 in numeros:
    pos_tres = numeros.index(3)
print(f'A)Quantidade de vezes que apareceu o numero 9: {contador_nove}')
print(f'B)Em que posição foi digitado o primeiro valor 3: {pos_tres+1}')
print(f'C) Numeros pares: {pares}')"""

