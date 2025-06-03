n, x, t = map(int, input().split())

if n % x == 0:
    res = int((n / x) * t)

else:
    res = int(((n // x) + 1) * t)

print(res)
