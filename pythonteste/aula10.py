"""nome = str(input('Qual e seu nome? '))
if nome == 'Theo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome e tao normal')
print(f'Bom dia {nome}!')"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua media foi {media:.1f}')

if media >= 6:
    print('Sua media ficou boa')
else:
    print('Sua media ficou ruim')