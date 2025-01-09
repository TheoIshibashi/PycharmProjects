#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

inicio = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZAO: '))
decimo = inicio + (10 - 1) * razao
for i in range(inicio, decimo + razao, razao):
    print(f'{i} ', end='-> ')
print('ACABOU')