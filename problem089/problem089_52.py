from collections import defaultdict as ddict

h,w,m=map(int,input().split())

xs=[0]*w
ys=[0]*h
xsmx=ysmx=0
pts=set()
for _ in range(m):
    y,x=map(int,input().split())
    x,y=x-1,y-1
    xs[x]+=1
    ys[y]+=1
    pts.add((x,y))
    xsmx=max(xsmx,xs[x])
    ysmx=max(ysmx,ys[y])

xsc=[x for x in range(w) if xs[x]==xsmx]
ysc=[y for y in range(h) if ys[y]==ysmx]
ans=xsmx+ysmx-1
ok=False
for y in ysc:
    for x in xsc:
        if (x,y) not in pts:
            ans+=1
            ok=True
            break
    if ok:
        break

print(ans)
