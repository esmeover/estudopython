velocidade = int(input('em qual velocidade voce passou(ex: 80 90 100): '))
multa = (velocidade-80)*7
if velocidade >= 81:
    print('voce foi multado em {}R$'.format(multa))
else:
    print('voce estava dentro do limite de velocidade')
