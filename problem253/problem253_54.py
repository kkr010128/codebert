n, a, b = map(int, input().split())
if (b - a) % 2 == 0:
    print((b-a) // 2)
    exit()
else:
    c = min(a - 1, n - b)
    print(c + (b - a + 1) // 2)
    exit()
