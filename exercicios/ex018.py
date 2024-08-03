import math
ang = float(input('angulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cos = math.cos(rad)
tangente = math.tan(rad)
print('o angulo {:.4f} tem o seno de {:.4f} cosseno de {:.4f} e a tangente {:.4f}'.format(ang, seno, cos, tangente))
