X, Y = map(int, input().split())

temp = [0, 300000, 200000, 100000]
ans = 0
if X == Y == 1:
    ans += 400000
if X <= 3:
    ans += temp[X]
if Y <= 3:
    ans += temp[Y]
print(ans)