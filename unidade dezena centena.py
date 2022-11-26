a = str ( input ('Digite um numero: ')).strip()
b = len (a) 
c = len (a) -1 
d = len (a) - 2
e = len (a) - 3 
print ('O valor das unidades é {}'.format(a[b-1]))
if ((c-1)<0):
    print ('Seu numero não é maior ou igual a 10')
    
else:
    print ('O valor das dezenas é {}'.format(a[c-1]))
if ((d-1)<0):
    print ('Seu numero não é maior ou igual a 100')
    
else:
    print ('O valor das centenas é {}'.format(a[d-1]))
if ((e-1)<0):
    print ('Seu numero não é maior ou igual a 1000')
    
else:
    print ('O valor das milhares é {}'.format(a[e-1]))