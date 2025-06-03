import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import combinations
def main():
    n, *a = map(int, read().split())
    coma = combinations(a, 3)
    r = 0
    for c in coma:
        if sum(c) > max(c)*2:
            if len(set(c)) > 2:
                r += 1
    print(r)

if __name__ == '__main__':
    main()
