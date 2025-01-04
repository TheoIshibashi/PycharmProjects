#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero: '))
print('Escolha uma base de conversao')
print('Digite: \n[ 1 ]Binario \n[ 2 ]: Octadecimal \n[ 3 ]: Hexadecimal')

conversao = int(input('Digite a base de conversao desejada: '))

if conversao == 1:
    print(f'{numero} convertido para binario é igual a {bin(numero)[2:]} ')
elif conversao == 2:
    print(f'{numero} convertido para octadecimal é igual a {oct(numero)[2:]}')
elif conversao == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print(f'{'\033[31m'}OPCAO INVALIDA! TENTE NOVAMENTE {'\033[m'}')