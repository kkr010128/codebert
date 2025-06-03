x, y = map(int, input().split())

ans = 0
if x + y == 2:
    ans += 400000

ans += ((4-min(4, x)) + (4-min(4, y))) * 100000

print(ans)