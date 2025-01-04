#Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la
#Sabendo que cada litro de tinta, pinta uma area de 2m2

largura = int(input('Digite a largura da parede em metros: '))
altura = int(input('Digite a altura da parede em metros: '))

area = largura*altura
litros = area / 2

print('Na area total de {} metros quadrados, sera necessario um total de {} litros de tinta!'.format(area, litros))