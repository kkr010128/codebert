a, b, k = map(int, input().split())
ans = 0

if k <= a:
    print(a-k, end=" ")
    print(b)
else:
    k -= a
    b = b - k if b - k >= 0 else 0
    print(0, end=" ")
    print(b)