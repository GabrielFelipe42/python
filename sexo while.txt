sexo = str(input('Qual o seu sexo ?[M/F]: ')).strip().upper()
while sexo not in ['M','F']:
        sexo = str(input ('Digite uma opção valida: ')).upper().strip()
print (f'Salvamos o seu sexo como {sexo}')