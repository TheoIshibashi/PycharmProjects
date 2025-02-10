#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
from queue import PriorityQueue

idade18 = 0
homem = 0
mulher20 = 0
print('-='*15)
print('CADESTRE UMA PESSOA')
print('-='*15)
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'HM':
        sexo = str(input('Qual o seu sexo? [H/M]')).strip().upper()
    if idade > 18:
        idade18 += 1
    if sexo == 'H':
        homem += 1
    elif sexo == 'M' and idade < 20:
        mulher20 += 1

    print('-'*30)
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()
    if escolha == 'N':
        break

print(20*'=','FIM DO PROGRAMA',20*'=')
print(f'A) Existem {idade18} pessoas com mais de 18 anos de idade.')
print(f'B) Existem {homem} homens cadastrados.')
print(f'C) Existem {mulher20} mulheres com menos de 20 anos de idade.')
