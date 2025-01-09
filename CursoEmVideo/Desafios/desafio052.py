# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('-='*20)
print('VERIFICADOR DE NUMEROS PRIMOS!!!')
print('-='*20)

numero = int(input('Digite um numero: '))
total_divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'{i} e divisor de {numero}')
        total_divisores = total_divisores + 1

if total_divisores == 2:
    print(f'O numero {numero} é primo!')
else:
    print(f'O numero {numero} nao e primo, pois tem {total_divisores} divisores')
