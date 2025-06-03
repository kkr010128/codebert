a,b,m = map(int,input().split())

r = tuple(map(int,input().split()))
d = tuple(map(int,input().split()))

ans = min(r)+min(d)

for i in range(m):
    x,y,c = map(int,input().split())
    ans = min(ans,r[x-1]+d[y-1]-c)
    
print(ans)