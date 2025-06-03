def gcd(a,b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b

a,b = list(map(int,input().split()))
print (gcd(a,b))