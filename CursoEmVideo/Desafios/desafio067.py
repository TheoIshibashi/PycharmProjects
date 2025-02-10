# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
contador = 0
contadorTabuadas = 0
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-'*20)

    for contador in range(1, 11):
        resultado = numero * contador
        print(f'{numero} x {contador} = {resultado}')
        contador += 1
    contadorTabuadas += 1
    print('-' * 20)
print(f'O programa foi finalizado. Foram solicitadas {contadorTabuadas} tabuadas')