itt = 0
it = 0
for c in range (1,3):
    print (f'---------[{c}]-------- Pessoa')
    nome = str (input (f'{c}-Digite seu nome: '))
    idade = int (input (f'{c}-Digite sua idade: '))
    it = it + idade
    sexo = print ('''Escolha qual é o seu sexo:
    [1]Feminino
    [2]Masculino''')
    sexo = int (input ('Escolha um: '))
    if sexo == 1:
        if idade < 20:
            itt = itt + 1
    else:
        if c==1:
            maior = idade
            nome2 = nome
        else:
            if idade > maior:
                maior = idade
                nome2 = nome
media = it/2
print (f'A media de idade do grupo é {media}')
print (f'A quantidade de mulheres menores de 20 é {itt}')
print (f'O homem com maior idade do grupo tem {maior} anos e se chama {nome2}')