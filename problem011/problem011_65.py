def gcd(x, y):
    while y != 0:
        temp = x % y
        x = y
        y = temp
    print x

l = map(int, raw_input().split())
gcd(*l)