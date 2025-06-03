n, a, b = map(int, input().split())
if a % 2 == b % 2:
    print((b - a) // 2)
else:
    if a > n - b + 1:
        rest = (b - a) // 2
        print(n - a - rest)
    else:
        rest = (b - a) // 2
        print(b - 1 - rest)
    #print(max(a, n - b + 1) - 1)