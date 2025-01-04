#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from xml.dom.minidom import ProcessingInstruction

radar = int(input('Digite a velocidade do carro (em km): '))
cores = {
    'limpa': '\033[m',
    'vermelho' : '\033[31m',
    'verde': '\033[32m'
}

vel_excesso = radar - 80
multa = vel_excesso * 7

if radar >= 80:
    print(f'{cores['vermelho']}VOCE FOI MULTADO!{cores['limpa']} A sua velocidade de {radar}km/h esta {vel_excesso}km/h acima do limite de velocidade de 80km/h.')
    print(f'{cores['vermelho']}Sua multa sera de R${multa:.2f}!{cores['limpa']}')
else:
    print(f'A sua velocidade de {radar}km/h esta dentro do limite de velocidade.')

print('Tenha um bom dia! Dirija com seguranca.')