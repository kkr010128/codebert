a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans = 123456789012345

for i in range(m):
    x,y,c=map(int,input().split())
    ans = min(ans, a[x-1]+b[y-1]-c)
a.sort()
b.sort()
ans = min(ans,a[0]+b[0])
print(ans)