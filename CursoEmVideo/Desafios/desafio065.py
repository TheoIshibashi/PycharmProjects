#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
soma = 0
maior = 0
menor = 0
continua = -1
while continua != 'N':
    numero = int(input('Digite um valor: '))
    if contador == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    soma += numero
    contador += 1
    continua = input('Deseja continuar o programa? \n[S - SIM]\n[N - NAO] ').upper()

media = soma / contador
print('=-'*20)
print(f'O maior valor foi {maior}.\nO menor valor foi {menor}\nE a media dos valores foi {media:.2f}')
print('=-'*20)
