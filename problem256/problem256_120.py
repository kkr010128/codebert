import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9
import fractions

def main():
    a,b = map(int, input().split())

    print(a*b//fractions.gcd(a, b))


if __name__ == '__main__':
    main()
