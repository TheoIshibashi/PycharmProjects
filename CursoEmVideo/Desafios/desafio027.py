"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = input('Digite seu nome completo: ').strip()
list_nome = nome.split()
first_name = list_nome[0]
last_name = list_nome[-1]
print(f'Primeiro nome: {first_name} \nUltimo nome: {last_name}')
