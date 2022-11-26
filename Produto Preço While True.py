produto = nome = e = ' '
preço = total = c = c1 = menor = 0
while True:
    produto = str (input ('Digite o nome do produto: '))
    preço = float (input ('Digite o preço do produto: '))
    if preço > 1000:
        c = c + 1
    total = total + preço
    c1 = c1 + 1
    if c1 == 1:
        menor = preço 
        nome = produto
    else:
        if preço<menor:
            menor = preço
            nome = produto
    e = str (input('Quer continuar as compras ?[S/N] ')).strip().upper()[0]
    if e == 'N':
        print ('Obrigado, volte sempre')
        break
print (f'O total gasto na compra foi {total:.2f} R$')
print (f'{c} Produto(s), custam mais de 1000,00 R$')
print (f'O produto com o menor preço é o/a {nome} e custa {menor:.2f} R$')