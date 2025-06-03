import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
from math import ceil
def main():
    n, x, t = map(int, input().split())
    print(ceil(n / x) * t)

if __name__ == '__main__':
    main()
