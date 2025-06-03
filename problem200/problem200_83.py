a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=min(a)+min(b)

for i in range(m):
    p,q,r=map(int,input().split())
    ans=min(a[p-1]+b[q-1]-r,ans)
print(ans)
