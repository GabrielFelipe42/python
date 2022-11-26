def maior(ist):
    pos = 0
    while pos < len(ist):
        if pos == 0:
            maior = ist[pos]
            menor = ist[pos]
        if pos > 0:
            if ist[pos] > maior:
                maior = ist[pos]
            if ist[pos] < menor:
                menor = ist[pos]
        pos = pos + 1
    print('='*30)
    print(f'O maior numero é {maior}')
    print(f'O menor numero é {menor}')
    print('='*30)
ist = list()
while True:
    n = int(input('Digite um valor: '))
    ist.append(n)
    e = str(input(('Voce quer continuar?[S/N] '))).strip().upper()[0]
    if e in 'N':
        break
maior(ist)