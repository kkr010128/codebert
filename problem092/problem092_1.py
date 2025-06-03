def resolve():
    import math
    x, k, d = list(map(int, input().split()))
    ans = abs(x)
    x = abs(x)
    if x - d * k >= 0:
        ans = x - d * k
    else:
        k -= math.floor(x / d)
        x -= math.floor(x / d) * d
        if k % 2 == 1: x = abs(x - d)
        ans = x
    print(ans)


resolve()
