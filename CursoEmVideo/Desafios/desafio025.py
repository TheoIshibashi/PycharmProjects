# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o seu nome: ').strip()

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'

}
if 'SILVA' in nome.upper():
    print(f'{cores['verde']}Seu nome possui Silva{cores['limpa']}')
else:
    print(f'{cores['vermelho']}Seu nome nao possui Silva{cores['limpa']}')


