n,d = map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

ans=0
for i in range(n):
    if x[i]**2+y[i]**2<=d**2:
        ans+=1

print(ans)