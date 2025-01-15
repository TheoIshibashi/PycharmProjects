#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
#Recebendo valores

print('GERADOR DE PA')
print('=-'*20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
contador = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo}', end=' -> ')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Operacao finalizada com {total} termos mostrados')










"""primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razao: '))

#inicializar variaveis

i = 1
termo = primeiro
contador = 10
escolha = -1

#comeco do while que verifica os 10 primeiros
while i <= contador:
    print('{}'.format(termo), end=' -> ')
    termo = termo + razao
    i = i + 1
#While para verificar se o usuario quer continuar, ou se quer adicionar mais termos
while escolha != 0:
    escolha = int(input('Deseja adicionar quantos termos? '))
    contador = contador + escolha
    while i <= contador:
        print('{}'.format(termo), end=' -> ')
        termo = termo + razao
        i = i + 1
print('CABO')"""
