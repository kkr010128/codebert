N,D = map(int,input().split())
xy = []
for i in range(N):
    x,y = map(int,input().split())
    xy.append([x,y])
ans = 0
for i in range(N):
    x = xy[i][0]
    y = xy[i][1]
    if(D*D >= (x*x + y*y)):
        ans+=1
print(ans)