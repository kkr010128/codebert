import sys
import fractions
def lcm(a,b):
    return int(a*b/fractions.gcd(a,b))

if __name__ == '__main__':
    for line in sys.stdin:
        a,b = map(int,line.split())
        print(int(fractions.gcd(a,b)),lcm(a,b))