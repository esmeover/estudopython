import random
numero = "0 1 2 3 4 5"
separar = numero.split()
random.shuffle(separar)
reposta = int(separar[0])
print('pensei em um numero tente adivinhar qual', end=' ')
usuario = input('de 0 a 5 digite qualquer um: ')
usuario = int(usuario)
if usuario == reposta:
    print('parabens voce acertou eu estava pensando {}'.format(reposta))
else:
    print('errou eu estava pensando no numero {}'.format(reposta))
