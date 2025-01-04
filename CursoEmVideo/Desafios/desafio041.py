"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER"""
from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - nascimento

if idade <= 9:
    print('Atelta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <=19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')