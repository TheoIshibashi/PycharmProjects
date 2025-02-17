"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

dados = dict()
aluno = list()
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input('Media: '))
if dados['Media'] >= 6:
    dados['Situacao'] = 'APROVADO'
else:
    dados['Situacao'] = 'REPROVADO'
aluno.append(dados.copy())

for dados in aluno:
    for chave, valor in dados.items():
        print(f'{chave} e igual a {valor}')
