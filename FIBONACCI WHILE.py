n = int (input ('Digite quantos termos vc quer ver: '))
c = 3
t1 = 0
t2 = 1
t3 = 1
print (t1, end =" ")
print (t2, end =' ')
while c<=n:
    t3 = t2 + t1
    print (t3, end = ' ')
    t1 = t2
    t2 = t3
    c= c +1
print ('Fim')