import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import floor
from decimal import Decimal

def main():
    x = int(input())
    n = Decimal(100)
    r = 0
    while n < x:
        n = Decimal(floor((n * 101 / 100)))
        r += 1
    print(r)

if __name__ == '__main__':
    main()
