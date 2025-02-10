#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
numero = int(input('Digite um valor: '))
lista.append(numero)
for i in range(0, 3):
    numero = int(input('Digite um valor: '))
    if numero < lista[0]:
        lista.insert(0, numero)
    else:
        lista.append(numero)
print(lista)
