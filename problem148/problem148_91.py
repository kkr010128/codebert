a, b, c, k = map(int, input().split())
if k <= a:
    print(int(k))
elif k <= a + b:
    print(int(a))
else:
    print(int(2*a + b - k))