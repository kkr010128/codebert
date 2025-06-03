def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x, y = [int(n) for n in input().split()]
print(gcd(x, y))