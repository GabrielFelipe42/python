import random
a = int (input('Digite um numero de 0 a 5: '))
b = random.randint (0,5)
print ('O valor de B foi {}'.format(b))
if (a==b):
    print ('Voce acertou o numero, parabens')
else:
    print ('Voce errou o numero, acontece')