def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

try:
    while 1:
        a,b = list(map(int,input().split()))
        c = gcd(a, b)
        print('{} {}'.format(c,int(c * (a/c) * (b/c))))

except Exception:
    pass