x, y = map(int, input().split())
ans = 100000*(max(4-x,0) + max(4-y,0))
if x == y == 1:
    ans += 400000
print(ans)
