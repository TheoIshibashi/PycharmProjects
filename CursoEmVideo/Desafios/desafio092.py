"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
import datetime
from datetime import date
cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.datetime.today().year - ano_nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho: '))
if cadastro['ctps'] != 0:
    cadastro['AnoContratacao'] = int(input('Ano de Contratacao: '))
    cadastro['Salario'] = float(input('Salario: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['AnoContratacao'] + 35) - datetime.datetime.now().year)

print('='*30)
for indice, valor in cadastro.items():
    print(f'{indice} tem o valor {valor}')
print('='*30)

