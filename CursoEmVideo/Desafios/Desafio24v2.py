# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome de uma cidade: ').strip()

if cidade[:5].upper() == 'SANTO':
    print(f'A sua cidade {cidade.capitalize()} comeca com Santo')
else:
    print(f'A sua cidade {cidade.capitalize()} nao comeca com Santo')
