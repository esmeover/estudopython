km = float(input('quantos km foram percorridos? '))
dia = int(input('quantos dias foram alugados? '))
val = km * 0.15 + dia * 60
print('O total a pagar é R${:.2f}'.format(val))
