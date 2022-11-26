n1 = int (input ('Digite o primeiro numero: '))
n2 = int (input ('Digite o segundo numero: '))
escolha = 0
while escolha !=5:
    print ('''Escolha uma operação da lista:
[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Digitar novos numeros
[5] Sair do programa''')
    escolha = int (input ('Digite sua escolha: '))
    if escolha == 1:
        print (f'{n1} + {n2} = {n1+n2}')
        
    elif escolha == 2:
        print (f'{n1} x {n2} = {n1*n2}')
        
    elif escolha == 3:
        if n1>n2:
            print (f'O maior valor é {n1}')
            
        else:
            print (f'O maior valor é {n2}')
            
    elif escolha == 4:
        n1 = int (input ('Digite o primeiro numero: '))
        n2 = int (input ('Digite o segundo numero: '))
if escolha == 5:
     print ('Fim do programa, Obrigado, volte sempre')