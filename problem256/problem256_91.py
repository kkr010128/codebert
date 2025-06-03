import math
def lcm(A, B):
    return int((A * B) / math.gcd(A, B))
A, B = map(int, input().split())
print(lcm(A,B))