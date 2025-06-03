A , B, M = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
res = min(a) + min(b)
for _ in range(M):
    x,y, c = list(map(int,input().split(" ")))
    x-=1
    y-=1
    res = min(res,a[x]+b[y]-c)
print(res)
