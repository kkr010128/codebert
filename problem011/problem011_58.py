#Greatest Common Diveser
def gcd(x, y):
    if x >= y:
        x = x % y
        if x == 0:
            return y
        return gcd(x, y)
    else:
        y = y % x
        if y == 0:
            return x
        return gcd(x, y)

x, y = map(int, input().split())
print(gcd(x, y))