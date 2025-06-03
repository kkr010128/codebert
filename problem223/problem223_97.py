n,k=map(int,input().split())
p=list(map(int,input().split()))
a=[None]*(n-k+1)
a[0]=sum(p[0:k])
for i in range(1,n-k+1):
    a[i]=a[i-1]-p[i-1]+p[i+k-1]
b=max(a)
c=(b/2)+(0.5*k)
print(c)