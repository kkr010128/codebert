x,y =  map(int,input().split())
ans = 0
for i in [x,y]:
    if i==3:ans+=100000
    elif i==2:ans+=200000
    elif i==1:ans+=300000
if x==y==1:
    ans += 400000
print(ans)