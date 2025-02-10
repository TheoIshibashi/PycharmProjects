#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
escolha = 'S'
while True:
    if escolha.upper() == 'S':
        numero = int(input('Digite um valor: '))
        lista.append(numero)
        escolha = input('Deseja continuar? [S/N]: ')
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    else:
        break

print(f'Lista completa: {lista}')
print(f'Lista com apenas pares: {pares}')
print(f'Lista com apenas impares {impares}')

