n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto e {} e a \n divisao e {:.3f}'.format(s, m, d), end=' ')
print('A divisao inteira e {} e a potencia e {}'.format(di, e))