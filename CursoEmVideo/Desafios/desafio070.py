"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
barato = ''
produtos_caro = 0
menor_preco = float('inf')
total = 0
print('-'*20)
print('LOJA SHIBAO')
print('-'*20)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor: R$'))
    total = total + preco
    if preco < menor_preco:
        menor_preco = preco
        barato = produto
    if preco > 1000:
        produtos_caro += 1
    escolha = input('Deseja continuar? [S/N]').strip().upper()
    if escolha == 'N':
        break

print(f'A) O total gasto da compra foi de R${total:.2f}')
print(f'B) A quantidade de produtos que custam mais de R$1000 foi de {produtos_caro}')
print(f'C) O nome do produto mais barato é: {barato} e custa R${menor_preco}')