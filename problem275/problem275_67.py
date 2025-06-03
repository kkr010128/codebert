X,Y = map(int,input().split())
ans = 0
shokin = [-1,300000,200000,100000]
if X in (1,2,3):
    ans += shokin[X]
if Y in (1,2,3):
    ans += shokin[Y]
if X == 1 and Y == 1:
    ans += 400000
print(ans)
