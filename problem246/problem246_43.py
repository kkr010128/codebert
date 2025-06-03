import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    l = sorted(list(itertools.permutations(range(1,n+1), n)))
    ans = []
    for i in range(len(l)):
        if l[i] == p:
            ans.append(i)
        elif l[i] == q:
            ans.append(i)
    if len(ans) == 1:
        print(0)
    else:
        print(abs(ans[0]-ans[1]))







if __name__=="__main__":
    main()
