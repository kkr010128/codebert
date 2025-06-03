N=int(input())
xy = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0

def dist(tpl1, tpl2):
    return abs(tpl1[0] - tpl2[0]) + abs(tpl1[1] - tpl2[1])

f0 = []
f1 = []
for i in range(N):
    x, y = xy[i]
    f0.append(x-y)
    f1.append(x+y)
ans = max(ans,
        max(f0) - min(f0),
        max(f1) - min(f1))
print(ans)