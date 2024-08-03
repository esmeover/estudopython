ano = int(input('digite um ano do calendário: '))
if ano % 4 == 0 and ano % 100 > 0:
        print('o ano é bisexto')
else:
    print('o ano nao é bisexto')