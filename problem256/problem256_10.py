from fractions import gcd
import sys
sys.setrecursionlimit(10**7)
a,b = map(int,input().split())
def lcm(x, y):
    return (x * y) // gcd(x, y)
if b != 0:
    print(lcm(a, b))
else:
    print(a)
