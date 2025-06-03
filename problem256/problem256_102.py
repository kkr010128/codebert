import sys
import fractions
input = lambda: sys.stdin.readline().rstrip()

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def main():
    a, b = map(int, input().split())
    print(lcm(a, b))

if __name__ == '__main__':
    main()