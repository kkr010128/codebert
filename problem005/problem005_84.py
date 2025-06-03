import math
while True:
    try:
        a, b = map(int, input().split())
        gcd = math.gcd(a, b)
        lcm = (a * b) // gcd
        print(gcd, lcm)
    except Exception:
        break

