#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
digitado = input('Digite uma expressao com parenteses: ')

for caractere in digitado:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if lista:
            lista.pop()
        else:
            print('Sua expressao esta incorreta!')
            break
else:
    if not lista:
        print('Sua expressao esta com parenteses corretamente!')
    else:
        print('Sua expressao esta incorreta!')


