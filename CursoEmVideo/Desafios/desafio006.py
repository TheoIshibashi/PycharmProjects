#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero: '))
num_dobro = numero * 2
num_triplo = numero * 3
num_raiz = numero ** (1/2)

print('O dobro de {} vale {}.'.format(numero, num_dobro)) #numero, (numero*2)
print('O triplo de {} vale {} \nA raiz quadrada de {} vale {:.2f}.'.format(numero, num_triplo, num_raiz))