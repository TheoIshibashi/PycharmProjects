# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
cores = {
    'limpa': '\033[m',
    'verde': '\033[32m'
}
viagem = int(input('Digite a distancia da viagem: '))

if viagem <= 200:
    preco = viagem * 0.5
    print(f'O valor da viagem ficou {cores['verde']}R${preco:.2f}{cores['limpa']}')
else:
    preco = viagem * 0.45
    print(f'O valor da viagem ficou {cores['verde']}R${preco:.2f}{cores['limpa']}')