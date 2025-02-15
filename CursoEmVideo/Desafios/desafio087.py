"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para: [{linhas}, {colunas}] '))

print('=-='*4)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
        if matriz[linhas][colunas] % 2 == 0:
            somaPar += matriz[linhas][colunas]
    print()
print('=-='*4)

for linhas in range(0,3):
    somaColuna += matriz[linhas][2]

for colunas in range(0, 3):
    if matriz[1][colunas] > maior:
        maior = matriz[1][colunas]

print(f'A soma de todos os valores pares digitados: {somaPar}')
print(f'A soma dos valores da terceira coluna:{somaColuna}')
print(f'O maior valor da segunda linha: {maior}')



