pr = float(input('qual o valor do produto: '))
d1 = float(input('quanto sera o valor do desconto em (ex: 5,10,20,50): '))
d2 = pr*d1/100
print('o preço do produto é {:.2f}, com o desconto ficara {:.2f} '.format(pr, pr-d2))