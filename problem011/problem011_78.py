def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if y == 0:
        return x
    return gcd(y, x % y)
x, y = map(int, input().split())
print(gcd(x, y))
