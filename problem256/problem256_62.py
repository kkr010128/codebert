def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

def abc148c_snack():
    a, b = map(int, input().split())
    print(lcm(a, b))

abc148c_snack()
