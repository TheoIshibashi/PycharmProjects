#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
}
ano = int(input('Que ano quer analisar? Digite 0 caso queira o ano atual: '))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{cores['verde']}O ano {ano} eh um ano bissexto{cores['limpa']}')
else:
    print(f'{cores['vermelho']}O ano {ano} nao eh um ano bissexto{cores['limpa']}')