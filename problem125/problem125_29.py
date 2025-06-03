from math import gcd

def lcm(a, b):
    return a * b / gcd(a, b)    

x = int(input())
ans = int(lcm(360, x) // x)
print(ans)