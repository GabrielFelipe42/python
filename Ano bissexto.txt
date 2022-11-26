a = int (input('Qual é o ano? '))
b = a - 2020
if ((b % 4) == 0):
    print ('O ano de {} é bissexto'.format(a))
else:
    print ('O ano de {} não é bissexto'.format(a))