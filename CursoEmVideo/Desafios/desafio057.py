#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

n = 1
sexo = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
