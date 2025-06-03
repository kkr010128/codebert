X, Y = map(int, input().split())
ans = 0
if X <= 3:
  ans += (4-X) * 100000
if Y <= 3:
  ans += (4-Y) * 100000
if X == Y == 1:
  ans += 400000
print(ans)