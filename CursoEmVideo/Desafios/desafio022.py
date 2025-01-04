"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ')

nome_upper = nome.upper()

nome_lower = nome.lower()

nome_tamanho = len(nome.replace(" ", ""))
nome_split = nome.split()
nome_primeiro = nome_split[0]
cont_nome_primeiro = len(nome_primeiro)

print(f'Seu nome em maisculas: {nome_upper} \nSeu nome em minisculas: {nome_lower} \nSeu nome tem ao todo: {nome_tamanho} letras \nSeu primeiro nome é {nome_primeiro} e ele tem {cont_nome_primeiro} letras')