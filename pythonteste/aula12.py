nome = str(input('Qual e o seu nome? '))
if nome == 'Theo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil')
elif nome in 'Monica Jessica Juliana Claudia':
    print('Belo nome feminino!')
else:
    print('Seu nome e bem normal.')
print(f'Tenha um bom dia {nome}!')