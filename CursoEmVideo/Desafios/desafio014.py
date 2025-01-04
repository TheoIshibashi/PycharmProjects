#Escreva um programa que converta uma temperatura digitada em C e converta para F

c = float(input('Digite a temperatura em graus celcius: '))

f = ((9 * c) / 5) + 32

print('A temperatura de {} Celcius corresponde a {} Farenheit.'.format(c, f))

