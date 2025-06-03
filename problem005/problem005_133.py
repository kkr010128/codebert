import sys
sys.setrecursionlimit(10**7)
import fileinput

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


for line in sys.stdin:
    x, y = map(int, line.split())
    print(gcd(x,y),lcm(x,y))
