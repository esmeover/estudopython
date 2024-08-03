salario = float(input('qual é o salario do funcionario: '))
if salario > 1.250 or 1250:
    novo_salario = 10*salario/100+salario
    print('com o aumento o salario ficará {}'.format(novo_salario))
else:
    novo_salario = 15*salario/100+salario
    print('com o aumento o salario ficará {}'.format(novo_salario))
exit()
