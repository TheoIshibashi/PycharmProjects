# Listas para armazenar informações
lista_nome = []
lista_idade = []
lista_sexo = []

# Variáveis para cálculos
soma_idades = 0
homem_mais_velho_nome = ''
homem_mais_velho_idade = 0
mulheres_menos_20 = 0

# Coleta de dados
for i in range(4):
    print(f'--- Pessoa {i + 1} ---')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite M para mulher e H para homem: ').strip().upper()

    # Adiciona informações às listas
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)

    # Soma das idades para média
    soma_idades += idade

    # Verifica se é homem e o mais velho
    if sexo == 'H' and idade > homem_mais_velho_idade:
        homem_mais_velho_idade = idade
        homem_mais_velho_nome = nome

    # Verifica se é mulher com menos de 20 anos
    if sexo == 'M' and idade < 20:
        mulheres_menos_20 += 1

# Resultados
media_idades = soma_idades / 4
print(f'\nA média de idade do grupo é {media_idades:.1f} anos.')
if homem_mais_velho_nome:
    print(f'O homem mais velho é {homem_mais_velho_nome}, com {homem_mais_velho_idade} anos.')
else:
    print('Não há homens no grupo.')
print(f'Há {mulheres_menos_20} mulher(es) com menos de 20 anos.')
