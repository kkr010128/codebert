n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
cheby = []
for i in range(n):
    l = [xy[i][0]-xy[i][1],xy[i][0]+xy[i][1]]
    cheby.append(l)

xmax = -10**10
xmin = 10**10
ymax = -10**10
ymin = 10**10
for i in range(n):
    if cheby[i][0] > xmax :
        xmax = cheby[i][0]
        xa = i
    if cheby[i][0] < xmin :
        xmin = cheby[i][0]
        xi = i
    if cheby[i][1] > ymax :
        ymax = cheby[i][1]
        ya = i
    if cheby[i][1] < ymin :
        ymin = cheby[i][1]
        yi = i

if abs(xmax-xmin) > abs(ymax-ymin):
    print(abs(xy[xa][0]-xy[xi][0])+abs(xy[xa][1]-xy[xi][1]))
else :
    print(abs(xy[ya][0]-xy[yi][0])+abs(xy[ya][1]-xy[yi][1]))
