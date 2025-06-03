n, a, b = [int(x) for x in input().split()]
if (b - a) % 2 == 0:
    print((b - a) // 2)
else:
    print(min(a, n - b + 1) + (b - a - 1) // 2)