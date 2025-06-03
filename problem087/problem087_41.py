import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
from math import ceil
def main():
    n = tuple(map(int, tuple(input())))
    if sum(n) % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()