import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
def main():
    ABC = LI()
    c = Counter(ABC)
    ans = len(c.values())

    if ans == 2:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
