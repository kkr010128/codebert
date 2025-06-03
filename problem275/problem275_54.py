X,Y = map(int,input().split())

price = [3*10**5, 2*10**5, 1*10**5]

ans = 0
if X == 1 and Y == 1:
    ans += 4*10**5

X -= 1
Y -= 1

if X < 3:
    ans += price[X]
if Y < 3:
    ans += price[Y]

print(ans)