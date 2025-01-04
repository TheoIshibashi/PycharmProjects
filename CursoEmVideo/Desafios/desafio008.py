#Escreva um valor que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Digite a quantidade de metros: '))

cm = metros * 100
mm = metros * 1000

print('Para {} metros, são {:.0f} centimetros e {:.0f} milimetros!'.format(metros, cm, mm))