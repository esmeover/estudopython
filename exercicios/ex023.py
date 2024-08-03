numero = str(input('digite um número: '))
if len(numero) >3:
    print('unidade', numero[3])
    print('dezena', numero[2])
    print('centena',  numero[1])
    print('milhar', numero[0])
else:
    print('o numero é menor q 4 digitos')