n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1** n2
# print('a soma entre',n1,'e',n2,' é',s)
print('a soma é {}, \n o produto é {} \n e a divisão é {}'.format(s, m, d,), end=' ')
print('a divisao inteira é{} e a potencia é {}'.format(di, e))
