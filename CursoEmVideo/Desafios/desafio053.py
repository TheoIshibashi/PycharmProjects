#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#print('VERIFICADOR DE PALINDROMO')

frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print(inverso, junto)
    print('Temos um palindro')
else:
    print(inverso, junto)
    print('Nao temos um palindro')