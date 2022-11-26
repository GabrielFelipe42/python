import random
print ('{:#^70}'.format(' Prazer, preparado para jogar Pedra, Papel ou Tesoura? '))
print ('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
e = int (input ('\nFaça sua escolha: '))
b = random.choice(['PEDRA','PAPEL','TESOURA'])
if e == 1:
    print ('Voce escolheu PEDRA e Eu escolhi {}'.format(b))
    if  b == 'PAPEL':
        print ('Voce Perdeu')
    elif b == 'TESOURA':
        print ('Voce Ganhou')
    else:
        print ('Empatamos')
elif e == 2:
    print ('Voce escolheu PAPEL e Eu escolhi {}'.format(b))
    if b == 'PEDRA':
        print ('Voce Ganhou')
    elif b == 'TESOURA':
        print ('Voce Perdeu')
    else:
        print ('Empatamos')
else:
    print ('Voce escolheu TESOURA e Eu escolhi {}'.format(b))
    if b == 'PEDRA':
        print ('Voce Perdeu')
    elif b == 'PAPEL':
        print ('Voce Ganhou')
    else:
        print ('Empatamos')