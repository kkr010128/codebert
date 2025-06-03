x, y = map(int, input().split())


def gcd(x, y):
    if x % y == 0:
        return y
    elif x % y == 1:
        return 1
    else:
        return gcd(y, x % y)

if x >= y:
    n = gcd(x, y)
    print(n)
else:
    n = gcd(y, x)
    print(n)