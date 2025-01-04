#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Qual o ano que o jovem nasceu? '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print(f'Quem nasceu em {ano} tem {idade} anos, Voce ainda vai se alistar no servico militar. \nSeu alistamento sera em {saldo} anos, em {atual + saldo}')
elif idade > 18:
    verificacao = input('Voce ja se alistou? \n[ Y ] Sim \n[ N ] Nao \n').upper()
    if verificacao == 'Y':
        print('PARABENS! Voce ja esta alistado.')
    else:
        saldo = idade - 18
        print(f'Quem nasceu em {ano} tem {idade} anos, Voce ja deveria ter se alistado a {saldo} anos em {atual - saldo}!!! ALISTE-SE AGORA!.')
elif idade == 18:
    print(f'Voce tem que se alistar IMEDIATAMENTE! Pois possui {idade} anos.')
else:
    print('Tu ta no erro parcero')
