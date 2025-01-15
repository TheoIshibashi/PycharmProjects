# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.
from random import randint
#Titulo do jogo
print('=-'*15)
print('TENTE ADIVINHAR QUAL NUMERO ESTOU PENSANDO...')
print('=-' * 15)

#Inicializacao de variaveis
acertou = False
palpites = 0
computador = randint(0, 10)

#Inicia o laco while e verifica se enquanto a variavel acertou nao for True ele continua rodando o input de novos palpites
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1

#Verifica se a escolha do usuario foi igual ao numero que o computador escolheu
    if jogador == computador:
        acertou = True
    else:
#Caso o usuario digite mais ou menos, exibe um print que da dica se o numero é maior que o digitado ou menor.
        if jogador < computador:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print(f'Voce acertou com {palpites} tentativas, Estava pensando no numero: {computador}')
