# Crie um programa que leia dois numeros e mostre a soma entre eles.

n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
cores = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}
soma = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['verde'],n1,cores['limpa'], cores['verde'],n2,cores['limpa'], cores['vermelho'], soma, cores['limpa']))
