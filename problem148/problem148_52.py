a, b, c, k = map(int, input().split())

if k >= a + b + c:
    print(a - c)
    exit()
elif k <= a:
    print(k)
elif k <= a + b:
    print(a)
    exit()
else:
    print(a - (k - a - b))
    exit()