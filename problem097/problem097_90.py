k=int(input())
if k%2==0 or k%5==0:
    print(-1)
else:
    i=1
    t=7
    while t%k!=0:
        i+=1
        t=(t*10+7)%k
    print(i)