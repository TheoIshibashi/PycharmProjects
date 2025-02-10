# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from queue import PriorityQueue

print('=' * 35)
print('CAIXA ELETRÔNICO'.center(35))
print('=' * 35)

#INPUT DE VALOR E INICIALIZACAO DE VARIAVEIS
saque = int(input('Digite o saque desejado: R$'))
#INICIALIZA CEDULA COMO 50 POR SER A MAIOR DISPONIVEL
cedula = 50
#VARIAVEL PARA CONTAR QUANTAS CEDULAS DE CADA VALOR SERAO UTILIZADAS
contador_cedulas = 0

#INICIO DO LACO WHILE PARA VERIFICAR SE O USUARIO AO FINAL DO PROGRAMA QUEIRA CONTINUAR.
while True:
    print('Cedulas entregues:')
#INICIO DO LACO WHILE QUE FAZ COM QUE ENQUANTO SAQUE FOR MAIOR QUE 0 ELE CONTINUARA REALIZANDO A ATIVIDADE DE CONTAGEM DE CEDULAS DE CADA VALOR,
#SUBITRAINDO O VALOR DO SAQUE PELO VALOR DA CEDULA ATUAL
    while saque > 0:
        if saque >= cedula:
            saque -= cedula
            contador_cedulas += 1
        else:
            if contador_cedulas > 0:
                print(f'R${cedula}: {contador_cedulas} cedulas')
            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            contador_cedulas = 0
    if contador_cedulas > 0:
        print(f'R${cedula}: {contador_cedulas} cedula(s)')
    print('=' * 35)
    escolha = input('DESEJA REALIZAR OUTRO SAQUE? [S/N] ').strip().upper()
    print('=' * 35)
    if escolha == 'N':
        print('OPERACAO FINALIZADA')
        break

