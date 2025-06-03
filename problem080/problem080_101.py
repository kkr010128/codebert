N = int(input())
u = []
v = []
for _ in range(N):
    x,y = map(int,input().split())
    u.append(x+y)
    v.append(x-y)

umax = max(u)
umin = min(u)
vmax = max(v)
vmin = min(v)

print(max(umax-umin,vmax-vmin))
