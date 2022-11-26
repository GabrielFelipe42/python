a = str(input('Digite seu nome: ')).strip()
b = a.split()
c = b[0]
d = b[len(b)-1]
print ('Seu primeiro nome é {}'.format(c))
print ('Seu ultimo nome é {}'.format (d))
