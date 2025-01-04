#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

notas1 = float(input('Digite a nota 1: '))
notas2 = float(input('Digite a nota 2: '))

media = (notas1 + notas2) / 2

print('A media entre {:.1f} e {:.1f} do aluno foi {:.1f}'.format(notas1, notas2, media))