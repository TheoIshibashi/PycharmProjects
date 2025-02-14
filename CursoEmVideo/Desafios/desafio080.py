#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(0, 5):
    numero = int(input('Digite um valor: '))
    if i == 0 or numero > lista[-1]:
        print('Foi adicionado ao final da lista...')
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1


print(f'Os valores digitados em ordem foram {lista}')