#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos.
#Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

alunos = [
    input('Digite o nome do primeiro aluno: '),
    input('Digite o nome do segundo aluno: '),
    input('Digite o nome do terceiro aluno: '),
    input('Digite o nome do quarto aluno: ')
]

random.shuffle(alunos)

print(f'A ordem ficou:')
for i, aluno in enumerate(alunos, start=1):
    print(f'{i}: {aluno}')