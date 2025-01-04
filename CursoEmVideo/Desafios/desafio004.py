# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

word = input('Digite algo ')

print('O tipo primitivo desse valor e {}'.format(type(word)))
print('So tem espacos? {}'.format(word.isspace()))
print('E um numero? {}'.format(word.isnumeric()))
print('E alfabetico? {}'.format(word.isalpha()))
print('E alfanumerico? {}'.format(word.isalnum()))
print('Esta em maisculas? {}'.format(word.isupper()))
print('Esta em minusuculas? {}'.format(word.islower()))
print('Esta capitalizado? {}'.format(word.istitle()))
