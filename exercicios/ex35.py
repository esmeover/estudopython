reta1 = float(input('digite o valor da primeira reta: '))
reta2 = float(input('da segunda: '))
reta3 = float(input('da ultima: '))
if reta1+reta2 > reta3 and reta1+reta3 > reta2 and reta2+reta3 > reta1:
    print('essas três retas formam um triangulo')
else:
    print('as tres retas nao formam um triangulo')
