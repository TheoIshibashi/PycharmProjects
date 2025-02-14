#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
#em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
escolha = 'S'
while True:
    if escolha.upper() == 'S':
        numero = int(input('Digite um numero: '))
        if numero not in lista:
            print('Valor adicionado com sucesso...')
            lista.append(numero)
        else:
            print('Valor duplicado, tente outro valor')
    elif escolha.upper() == 'N':
        break
    else:
        print('Selecione S ou N apenas.')
    escolha = input('Deseja continuar? [S/N]: ')

print(f'Lista finalizada. Os valores unicos da lista em ordem sao: {sorted(lista)}')
