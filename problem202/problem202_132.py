n, a, b = map(int, input().split())

s, e = divmod(n, (a + b))

if e >= a:
    print(s * a + a)
else:
    print(s * a + e)