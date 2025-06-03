import math
A, B = [int(s) for s in input().split(' ')]
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(A, B))
