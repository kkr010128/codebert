def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while y != 0:
        x, y = y, x % y
    return x

X, Y = (int(s) for s in input().split())
print(gcd(X, Y))