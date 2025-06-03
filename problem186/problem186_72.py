k,n=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
    if i<n-1:
        b[i]=a[i+1]-a[i]
    else:
        b[n-1]=a[0]+k-a[n-1]
b.sort()
print(sum(b[:n-1]))