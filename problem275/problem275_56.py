X,Y = map(int,input().split())
money = [300000,200000,100000]
ans = 0
if X - 1 < 3:
	ans += money[X - 1]
if Y - 1 < 3:
	ans += money[Y - 1]
if X == 1 and Y == 1:
	ans += 400000
print(ans)