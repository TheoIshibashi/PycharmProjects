#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

dinheiro = float(input('Digite o seu saldo: R$'))
dolar = 6.12
euro = 6.33
iene = 0.039
conv_dolar = dinheiro / dolar
conv_euro = dinheiro / euro
conv_iene = dinheiro / iene

print('Com {:.2f} Você pode comprar: \n{:.2f} dolares \n{:.2f} euros \n{:.2f} ienes \nConsiderando os valores do dolar em R$6.12, euro em 6.33 e iene a 0.039 Reais'.format(dinheiro, conv_dolar, conv_euro, conv_iene))