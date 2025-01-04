#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

av1 = float(input('Digite a primeira nota: '))
av2 = float(input('Digite a segunda nota: '))

media = (av1 + av2) / 2

if media < 5:
    print(f'{'\033[31m]'}REPROVADO com media {media}{'\033[m'}')
elif 5 < media < 7:
    print(f'{'\033[33m'}RECUPERAÇÃO com media {media}{'\033[m'}')
else:
    print(f'{'\033[32m'}APROVADO com media {media}{'\033[m'}')
