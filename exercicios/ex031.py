viagem = float(input('quantos kilometros voce irá viajar: '))
if viagem <=200:
    calculo = 0.5*viagem
    print('voce tera que pagar {:.2f}R$'.format(calculo))
else:
    calculo = 0.45*viagem
    print('voce tera que pagar {:.2f}R$'.format(calculo))