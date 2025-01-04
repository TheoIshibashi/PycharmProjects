#Faca um algoritmo que leia o salario e mostre o seu novo salario, com 15% de aumento

salario = float(input('Digite o seu salario: '))

aumento = salario * 1.15
#aumento = salario * 0.15 -> salario + aumento mesma coisa tbm

print('O seu novo salario com 15% de aumento é {:.2f} Reais'.format(aumento))

