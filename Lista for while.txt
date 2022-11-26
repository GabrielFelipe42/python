lista = list()
for c in range (1,6):
    lista.append(int(input(f'Digite o um valor na posição {c}: ')))
print ('\nA sua lista ficou assim:')
for c,v in enumerate(lista):
    print (f'{v:.<30} na posição {c:>}')



print (f'O maior valor da lista é {max(lista)}, na posição ', end ='')
for c,v in enumerate(lista):
    if v == max(lista):
        print (f'{c}...', end = '')
print ()
print (f'O menor valor da lista é {min(lista)}, na posição ', end ='')
for c,v in enumerate(lista):
    if v == min(lista):
        print (f'{c}...', end = '')
