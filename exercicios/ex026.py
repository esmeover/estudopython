frase = input('digite um frase: ')
print('existem', frase.upper().count('A'), 'AS')
print('o A aparece a primeira vez no caractere:', frase.upper().find('A'))
print('a ultima vez que A aparece é na posiçao', frase.upper().rfind('A'))
