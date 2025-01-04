"""
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').upper().strip()
count_A = frase.count('A')
first_A = frase.find('A')+1
last_A = frase.rfind('A')+1

print(f'Frase: {frase.capitalize()} \nA letra A aparece: {count_A} \nA primeira letra A aparece na posicao: {first_A} \nA ultima letra A aparece na posicao {last_A}')