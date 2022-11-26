a = float (input ('Digite o primeiro valor: ' ))
b = float (input ('Digite o segundo valor: '))
c = float (input ('Digite o terceiro valor: '))
if (a>b) and (a>c):
    print ('O {} é o maior valor'.format(a))
if (b>a) and (b>c):
    print ('O {} é o maior valor'.format(b))
if (c>a) and (c>b):
    print ('O {} é o maior valor'.format(c))
if (a<b) and (a<c):
    print ('O {} é o menor valor'.format(a))
if (b<a) and (b<c):
    print ('O {} é o menor valor'.format(b))
if (c<a) and (c<b):
    print ('O {} é o menor valor'.format(c))