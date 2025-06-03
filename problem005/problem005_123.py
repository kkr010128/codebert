import math
while 1:
    try:
        a,b = map(int, input().split())
        print(math.gcd(a,b), int(a*b/math.gcd(a,b)))
    except:
        break
