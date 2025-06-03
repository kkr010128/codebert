x, y = (int(x) for x in input().split())
if x == y == 1: print(1000000)
else:
    ans = 0
    points = [300000, 200000, 100000]
    if x <= 3: ans += points[x-1]
    if y <= 3: ans += points[y-1]
    print(ans)
