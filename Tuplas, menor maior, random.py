from random import randint 
a = randint (0,40)
b = randint (0,40)
c = randint (0,40)
d = randint (0,40)
e = randint (0,40)
tupla = (a,b,c,d,e)
z = 1
print (f' Os valores sorteados foram {tupla}')
while z != 6:
    if z == 1:
        menor = tupla[z-1]
        maior = tupla[z-1]
    else:
        if tupla[z-1]>maior:
            maior = tupla[z-1]
        
        if tupla[z-1]<menor:
            menor = tupla[z-1]
    z = z + 1
print (f'O maior valor é {maior}')
print (f'O menor valor é {menor}')

print (f'\nO maior valor é {max(tupla)}')
print (f'O menor valor é {min(tupla)}')