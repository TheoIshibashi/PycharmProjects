#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
}
salario = float(input('Digite o seu salario: '))

if salario >= 1250.00:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print(f'{cores['vermelho']} Quem ganhava {salario:.2f}{cores['limpa']} {cores['verde']}Passa a ganhar {aumento:.2f}{cores['limpa']}')