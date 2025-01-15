#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#input das informacoes do usuario
sequencia = int(input('Numero de elementos da sequencias: '))

#inicializacao de variaveis
valor1 = 0
valor2 = 1

print(f'{valor1} -> {valor2}', end='')
#Comeca a contar do 3 pq ja recebeu dois valores.
contador = 3

#inicio do laco
while contador <= sequencia:
    #salva o valor3 sendo o resultado da soma do primeiro e segundo valor, no caso 0 + 1 no primeiro laco.
    valor3 = valor1 + valor2
    print(f' -> {valor3}', end='')

    #Reordena o valor das variaveis.
    valor1 = valor2
    valor2 = valor3

    #Adiciona +1 valor para o contador, para que ele chegue ate o valor da variavel sequencia
    contador = contador + 1
print(' -> Acabou')


