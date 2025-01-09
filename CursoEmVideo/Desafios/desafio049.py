# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
import time

print('TABUADAO CABULOSO')

tabuada = int(input('Digite o numero que deseja ver a tabuada: '))
print('CALCULANDO RESULTADOS...')
time.sleep(2)
for i in range(1, 11):
    resultado = tabuada * i
    print(f'{tabuada} x {i} = {resultado}')
print('Tabuada finalizada')