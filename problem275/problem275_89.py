X, Y = map(int, input().split(" "))

d = {1: 300000, 2: 200000, 3: 100000}
ans = 0
ans += d.get(X, 0)
ans += d.get(Y, 0)
if X == 1 and Y == 1:
    ans += 400000

print(ans)
