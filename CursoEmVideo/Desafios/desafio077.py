#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Aprender', 'Programar', 'Linguagem', 'PYTHON', 'Curso', 'Descreve')
print('VOGAIS :)')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=', ')

