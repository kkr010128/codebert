n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x + y)
    ys.append(x - y)
xs.sort()
ys.sort()
ans = max(xs[-1] - xs[0], ys[-1] - ys[0])
print(ans)
