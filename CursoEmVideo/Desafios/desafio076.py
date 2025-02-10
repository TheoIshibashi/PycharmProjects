#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ['caixa', 10.00, 'suco', 15.00, 'chocolate', 5.00, 'banana', 2.00]
print('-'*40)
print('LISTAGEM DE PRECOS'.center(40))
print('-'*40)
for pos in range (0, len(produtos), 2):
    print(f'{produtos[pos].title().ljust(34)}', end='')
    print(f'{produtos[pos+1]:>6.2f}')
print('-' * 40)