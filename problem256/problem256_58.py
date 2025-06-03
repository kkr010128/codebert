def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            c = a
            a = b
            b = c
        b %= a
    return max(a,b)

a,b = map(int,input().split())
print(a*b//gcd(a,b))