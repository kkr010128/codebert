a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[list(map(int,input().split())) for _ in range(m)]
ans=min(a)+min(b)
for x,y,c in l:
    ans=min(ans,a[x-1]+b[y-1]-c)
print(ans)