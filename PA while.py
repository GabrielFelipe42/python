p = int ( input ( 'Digite o primeiro termo da PA: '))
r = int ( input ( 'Digite a razão da PA: '))
c = 0
n = int (input ('Quantos termos vc quer ver? '))
while c <= n:
    p = p + r*c
    c = c+1
    print (p)
    if c == n:
        p2 = int (input ('Quantos termos mais vc quer ver? '))
        if p2 > 0:
                n = n + p2
                
        else:
                print ('Fim, volte sempre')
                break