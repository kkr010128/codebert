import math
while True:
    try:
        a = list(map(int,input().split()))
        b = (math.gcd(a[0],a[1]))
        c = ((a[0]*a[1])//math.gcd(a[0],a[1]))
        print(b,c)
    except EOFError:
        break
