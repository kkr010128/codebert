import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    ans = 0
    for n in range(1,N+1):
        ans += (N//n)*(2*n+(N//n-1)*n)//2
    print(ans)


if __name__ == '__main__':
    main()