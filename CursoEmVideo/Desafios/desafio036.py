#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Entrada de dados
salario = float(input('Informe o Salario: R$'))
casa = float(input('Qual o valor da casa? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

#Validacao dos dados
if salario <= 0 or casa <= 0 or anos <= 0:
    print('Erro: Todos os valores devem ser maiores que zero.')
else:
    #Calculos
    meses = anos * 12
    prestacao = casa / meses
    limite = salario * 0.3

        #Decisao
    if prestacao >= limite:
        print(f'EMPRÉSTIMO NEGADO! A prestação mensal de R$ {prestacao:.2f} excede o limite de R$ {limite:.2f} (30% do salário).')
    else:
        print(f'EMPRÉSTIMO APROVADO! A prestação será de R$ {prestacao:.2f}, em {meses} meses.')
