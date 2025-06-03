def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y

    return y


x, y = map(int, input().split())
print(gcd(x, y))
