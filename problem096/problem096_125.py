n,d= map(int, input().split())
xy = [list(map(int,input().split())) for _ in range(n)]
c= 0
for x,y in xy:
    if x**2+y**2 <= d**2:
        c += 1
print(c)