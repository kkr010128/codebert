n,m = map(int,input().split())
if(n % 2 == 0):
    d = n // 2 - 1
    c = 0
    i = 1
    while(d > 0):
        print(i,i+d)
        d -= 2
        i += 1
        c += 1
        if(c == m):exit()
    d = n // 2 - 2
    i = n // 2 + 1
    while(d > 0):
        print(i,i+d)
        d -= 2
        i += 1
        c += 1
        if(c == m):exit()


else:
    for i in range(m):
        print(i+1,n-i)
