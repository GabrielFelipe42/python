from random import randint
c = 0
j = 0
n = 0
pc = 0
while True:
    print ('''
[1] - Par
[2] - Impar ''')
    j = int(input ('Escolha digitando o valor: '))
    n = int(input ('Agora digite o seu valor: '))
    pc = randint(1,10)
    print (f'O valor escolhido pelo computador foi {pc}')
    if j == 1:
        if (n+c)%2 == 0:
            print ('Vc Ganhou!!!!!')
            c = c+ 1
        else:
            print ('Vc Perdeu!!!!')
            break
    else:
        if (n+c)%2 == 0:
           print ('Vc Perdeu!!!!')
           break
        
        else:
            print ('Vc Ganhou!!!!')
            c = c + 1
print (f'Vc ganhou {c} veze(s)')