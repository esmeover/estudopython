import random
al1 = input('primeiro aluno: ')
al2 = input('segundo aluno: ')
al3 = input('terceiro aluno: ')
al4 = input(' ultimo aluno: ')
print('dos alunos {}, {}, {} e {} o vencedor é: '.format(al3, al2, al1, al4), end=' ')
print('o ganhadoré{}'.format(random.choices([al4, al3, al2, al1])))
