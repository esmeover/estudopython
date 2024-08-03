import math
c = float(input('digite o valor do cateto oposto: '))
b= float(input('digite o valor do cateto adjacente: '))
a = (c**2 + b**2) ** (1/2)
print('a hipotenusa do triangulo retangulo é {:.2f}'.format(a))
hi = math.hypot(c, b)
print('a hipotenusa do triangulo retangulo é {:.2f}'.format(hi))