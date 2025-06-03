x, k, d = map(int, input().split())
if abs(x) // d >= k:
    if x > 0:
        print(x - k * d)
    else:
        print(abs(k * d + x))
    exit()
div = abs(x) // d
k -= div
if x > 0:
    x -= div * d
else:
    x += div * d
if k % 2 == 0:
    print(abs(x))
else:
    print(abs(abs(x) - d))
