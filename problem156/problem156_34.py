x = int(input())
d= {}
for a in range(10**25):
    #print(a,d)
    a5 = a**5
    b5 = a5-x
    if b5 in d:
        print(a,d[b5])
        exit()
    d[a5] = a
    #print('--------------',a,d)
    a5 = -a5
    b5 = a5-x
    if b5 in d:
        print(a,d[b5])
        exit()
    d[a5] = -a



