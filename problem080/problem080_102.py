n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

xy.sort(key=lambda x: x[0] + x[1])
mn1, mx1 = xy[0], xy[-1]
xy.sort(key=lambda x: x[0] - x[1])
mn2, mx2 = xy[0], xy[-1]

li = [mn1, mx1, mn2, mx2]
ans = 0
for x1, y1 in li:
    for x2, y2 in li:
        dist = abs(x1 - x2) + abs(y1 - y2)
        ans = max(ans, dist)

print(ans)
