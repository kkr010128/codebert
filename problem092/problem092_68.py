x, k, d = map(int, input().split())
if x < 0:
    target = abs(x) // d
    x = x + d * min(target, k)
    k -= min(target, k)
else:
    target = x // d
    x = x - d * min(target, k)
    k -= min(target, k)
if k % 2 != 0:
    if x < 0:
        x += d
    else:
        x -= d
print(abs(x))
