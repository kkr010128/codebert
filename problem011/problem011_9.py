def gcd(a,b):
    x,y = (a,b) if a>b else (b,a)
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

a,b = map(int, input().split())
print(gcd(a,b))