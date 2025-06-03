i=0
while True:
    N=int(input())
    if N==0:
        break
    else:
        a = list(map(float,input().split()))
        m=sum(a)/N
        #print(m)
        for i in range(N):
            a[i]=(float)(a[i]-m)**2
            #print(a[i])
            i+=1
        
        A=(sum(a)/N)**(1/2)
        print(A)
        
