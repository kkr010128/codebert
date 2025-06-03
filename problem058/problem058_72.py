while True:
    n, x = list(map(int,input().split()))
    m=0
    if n==0 and x==0:
        break
    else:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1, n+1):
                    #print(i,j,k)
                    if i+j+k==x:
                        m+=1
    print(m)