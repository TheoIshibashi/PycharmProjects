#Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto

preco = float(input('Digite o valor do produto: '))

desconto = preco * 0.05
#desconto = preco * 0.95 mesma coisa tambem
total = preco - desconto

print('O preco do produto com o desconto é {} Reais.'.format(total))
