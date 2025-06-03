X, Y = map(int, input().split())
ans = max(4 - X, 0) + max(4 - Y, 0)
if X == 1 and Y == 1:
    ans += 4
print(ans * 100000)
