f=lambda:map(int,input().split())
A,B,m=f()
a=list(f())
b=list(f())
ans=min(a)+min(b)
for _ in range(m):
    x,y,c=f()
    ans=min(ans,a[x-1]+b[y-1]-c)
print(ans)    