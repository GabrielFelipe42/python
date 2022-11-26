import math
a = float ( input ('Digite o valor do Angulo em Graus: '))
b = math.radians(a)
print ('O Angulo {} Tem Seno = {:.2f}, cosseno = {:.2f} e Tangente = {:.2f}'.format(a,math.sin(b),math.cos(b),math.tan(b)))