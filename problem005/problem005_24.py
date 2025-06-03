import sys

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

for line in sys.stdin:
    a,b = map(int, line.split())
    if a<b:
        tem = a
        a = b
        b = tem
    gc = gcd(a,b)
    print(gc, a*b//gc)