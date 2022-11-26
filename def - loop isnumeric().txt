def  leiaint(msg):
    while True:
        if msg.isnumeric():
            return(f'{msg} É um numero, parabens!!!')
            break
        else:
            print(f'{msg} Não é um numero, digite outra coisa!!!')
            msg=str(input('Digite novamente: '))
        
        
        


print(leiaint(str(input('Digite algo: '))))