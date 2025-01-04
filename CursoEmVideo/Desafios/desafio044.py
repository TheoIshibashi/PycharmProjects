"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros
"""

produto = float(input('Digite o valor do produto: R$'))
print('Calculador de valor: \n[1]A vista no dinheiro ou cheque. 10% de desconto\n[2]A vista no Cartao. 5% de desconto\n[3]Em ate 2x no cartao. Valor normal\n[4]3x ou mais no cartao. 20% de juros')
metodo = int(input('Qual a forma de pagamento: '))
if metodo == 1:
    desconto = produto * 0.90
    print(f'O valor a ser pago fica em R${desconto}')
elif metodo == 2:
    desconto = produto * 0.95
    print(f'O valor a ser fica em R${desconto}')
elif metodo == 3:
    print(f'O valor a ser pago fica em R${produto}')
elif metodo == 4:
    acrescimo = produto * 1.20
    print(f'O valor a ser pago fica em R${acrescimo}')
else:
    print('OPCAO INVALIDA, TENTE NOVAMENTE')