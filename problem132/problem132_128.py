n,k=map(int,input().split())
a=list(map(int,input().split()))
c=[n for i in range(n)]
for j in range(k):
    d=[0 for i in range(n+1)]
    for i in range(n):
        d[max(i-a[i],0)]+=1
        d[min(i+a[i]+1,n)]-=1
    e=[d[0]]
    for i in range(n-1):#ちょっと特殊な累積和 普通のものの[1:-1]
        e.append(e[i]+d[i+1])
    #print(d,e,sep='\n')
    #print(e)
    a=e
    if e==c:
        break
print(*a)
