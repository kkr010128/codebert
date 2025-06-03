import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import pi
def main():
    n, *a = map(int, read().split())
    cnt = [0] * n
    for ae in a:
        cnt[ae-1] += 1
    print(*cnt, sep='\n')

if __name__ == '__main__':
    main()
