lista = list()
dic = dict()


def notas(*num,msg = ''):
    s = 0
    c = 0
    while True:
        n = float(input('Digite sua Nota: '))
        lista.append(n)
        c = c + 1
        s = s + n
        e = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if e == 'N':
            break
    med = s/c
    msg = str(input('Qual é a situação? ')).strip()
    if msg in '':
        msg = 'Desconhecida'
    dic = {'Quantidade de notas': len(lista),'A maior nota': max(lista),'A menor nota': min(lista), 'Media da turma': med,'Situação': msg}
    print('='*30)
    for c,v in dic.items():
        print(f'{c}...{v}')
    print('='*30)


notas()