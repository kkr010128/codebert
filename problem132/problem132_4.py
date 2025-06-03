n,k=map(int,input().split())
a=list(map(int,input().split()))

for l in range(k):
    if a==[n]*n: 
        break
    imos = [0]*(n+1)
    for i in range(n):
        imos[max(0,i-a[i]) ]+=1
        imos[min(n-1,i+a[i])+1 ]-=1

    a=[0]*n
    a[0]=imos[0]
    for i in range(1,n):
        a[i] = a[i-1]+imos[i]

print(*a) 