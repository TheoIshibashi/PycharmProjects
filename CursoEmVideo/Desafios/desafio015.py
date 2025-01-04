#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

day = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

day_price = 60.0
km_price = 0.15

value_day = day * day_price
value_km = km * km_price
total_value = value_km + value_day

print(f'O carro foi alugado por {day} dias e custou R${value_day}, considerando R$60 o dia \nAndou {km}km e custou R${value_km:.2f}, considerando R$0.15 por km. \nO total a se pagar ficou em R${total_value:.2f}')