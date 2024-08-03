import random
al1 = str(input('aluno: '))
al2 = str(input('aluno: '))
al3 = str(input('aluno: '))
al4 = str(input('aluno: '))
r = random.sample([al1,al2, al3, al4], k=4)
print(' a ordem de apresentação sera de: ', end=' ')
print(r)
