#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
from random import choice
'''
    n1 = input('Digite o nome do primeiro aluno: '),
    n2 = input('Digite o nome do segundo aluno: '),
    n3 = input('Digite o nome do terceiro aluno: '),
    n4 = input('Digite o nome do quarto aluno: ')
    
alunos = [n1, n2, n3, n4]
mesma coisa que o de baixo
'''
alunos = [
    input('Digite o nome do primeiro aluno: '),
    input('Digite o nome do segundo aluno: '),
    input('Digite o nome do terceiro aluno: '),
    input('Digite o nome do quarto aluno: ')
]

sorteio = choice(alunos)

print(f'O aluno escolhido para apagar o quadro foi: {sorteio}')


