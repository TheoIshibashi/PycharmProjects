# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
}
cidade = input('Digite o nome da sua cidade: ').strip()

if cidade[:5].upper() == 'SANTO':
    print(f'Sua cidade {cidade.capitalize()} {cores['verde']}comeca com Santo{cores['limpa']}')
else:
    print(f'Sua cidade {cidade.capitalize()} {cores['vermelho']}nao comeca com Santo{cores['limpa']}')
