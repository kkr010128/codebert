n,d=map(int, input().split())
xy=[]
ans = 0
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])
    if d**2>=x**2+y**2:
        ans += 1
print(ans)
