print ('{:#^40}'.format(' Bem vindo a Loja do Gabas '))
p = float (input ('Digite o valor das suas compras: '))
print ('''Escolha a sua forma de PAGAMENTO:
1 - A vista (CHEQUE/DINHEIRO)
2 - A vista no CARTÃO
3 - PARCELADO em 2x
4 - PARCELADO em 3x ou mais''')
d = int(input ('Aviso!Cada forma de pagamento tem um respectivo desconto:  '))
if (d == 1):
    print ('O valor a ser pago é de {:.2f}R$ no DINHEIRO OU CHEQUE a vista'.format(0.9*p))
elif (d == 2):
    print ('O valor a ser pago é de {:.2f}R$ no CARTÃO a vista'.format(0.95*p))
elif (d == 3):
    print ('O valor a ser pago é de {:.2f}R$ PARCELADO em 2x no CARTÃO'.format(p))
elif (d == 4):
    print ('O valor a ser pago é de {:.2f}R$ PARCELADO em 3x ou mais no CARTÃO'.format(1.2*p))