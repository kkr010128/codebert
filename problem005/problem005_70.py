import sys

def gcd(a, b):
    return gcd(b, a % b) if a % b else b

def lcm(a, b):
    return a * b / gcd(a, b)

for line in sys.stdin:
    data = map(int, line.split())
    a, b = data
    print "%d %d" % (gcd(a, b), lcm(a, b))