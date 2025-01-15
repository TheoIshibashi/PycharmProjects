#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('=-'*20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
contador = 1
termo = primeiro
while contador <= 10:
    print(f'{termo}', end=' -> ')
    termo = termo + razao
    contador = contador + 1
print('CABO')

