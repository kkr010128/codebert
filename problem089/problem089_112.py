import collections

h,w,m = map(int,input().split())

gyou = [0 for i in range(h)]
retu = [0 for i in range(w)]
l = []

for i in range(m):
    y,x = map(int,input().split())
    gyou[y-1] += 1
    retu[x-1] += 1
    l.append((y-1,x-1))

ymax = max(gyou)
xmax = max(retu)
c_ymax = gyou.count(ymax)
c_xmax = retu.count(xmax)
ans = ymax + xmax

c = 0
for y,x in l:
    if gyou[y] == ymax and retu[x] == xmax:
        c += 1

if c == c_ymax*c_xmax:
    print(ans-1)
else:
    print(ans)