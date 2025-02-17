"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoas = dict()
lista = list()
mulheres = list()
idadeAcima = list()
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Masculino ou Feminino? [M/F] '))
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
#Verifica se a pessoa eh mulher
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy())

    soma += pessoas['idade']
    media = soma / (len(lista))
    if pessoas['idade'] > media:
        idadeAcima.append(pessoas.copy())

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break


print(f'Foram cadastradas {len(lista)}')
print(f'A media de idade foi de {media}')
print(f'Lista so com mulheres: {mulheres}')
print(f'Pessoas com idade maior que a media: {idadeAcima}')

