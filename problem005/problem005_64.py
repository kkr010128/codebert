import sys

def gcd(a, b):
    while b % a:
        a, b = b % a, a
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

for line in sys.stdin:
    a, b = sorted(list(map(int, line.split())))
    print(gcd(a, b), lcm(a, b))