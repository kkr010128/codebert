import math
n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

a_lcm = 1
for ai in a:
    a_lcm = lcm(a_lcm, ai)

b_sum = 0
for ai in a:
    b_sum += a_lcm // ai

print(b_sum%mod)
