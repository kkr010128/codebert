x, k, d = map(int, input().split())
if x < 0:
    x = -x
if k * d <= x:
    print(x - k * d)
else:
    t = x // d
    x -= t * d
    k -= t
    if x >= d:
        x -= d
        k -= 1
    if k % 2 == 1:
        x -= d
    print(abs(x))
