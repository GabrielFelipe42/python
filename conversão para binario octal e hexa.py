n = int ( input ( 'Diite um numero inteiro: '))
print ('''Escolha Uma das Opções de CONVERSÃO
[1] Para converter em BINARIO
[2] Para converter em OCTAL
[3] Para converter em HEXA''')
opçao = int (input ('Sua escolha: '))
if opçao == 1:
    print ('O {} em BINARIO é {}'.format(n, bin(n)[2:]))
elif opçao == 2:
    print ('O {} em OCTAL é {}'.format(n, oct(n)[2:]))
elif opçao == 3:
    print ('O {} em HEXA é {}'.format(n, hex(n)[2:]))
else:
    print ('Essa opção não existe')