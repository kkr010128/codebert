while True:
    n,x=[int(i) for i in input().split()]
    if n==x==0:
        break
    c = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if (i+j+n >= x):
                for k in range(j+1,n+1):
                    if(i+j+k == x):
                        c+=1
                        break

    print(c)