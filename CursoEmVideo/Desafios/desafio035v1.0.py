#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'ciano': '\033[36m'
}
print(f'{cores['ciano']}-={cores['limpa']}' * 20)
print('Analisador de formacao de triangulos')
print(f'{cores['ciano']}-={cores['limpa']}' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2+r3 or r2 < r1+r3 or r3 < r1+r2:
    print(f'{cores['verde']}Os segmentos acima podem formar triangulo{cores['limpa']}')
else:
    print(f'{cores['vermelho']}Os segmentos nao podem formar triangulo{cores['limpa']}')

