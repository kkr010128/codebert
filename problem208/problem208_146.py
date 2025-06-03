import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n,m = map(int, input().split())
    ans = [0]*n

    for i in range(m):
        s,c = map(int, input().split())
        if n > 1 and s-1 == 0 and c == 0: # 2桁以上先頭0
            print(-1)
            exit()
        if ans[s-1] in [0,c]: # 入力なし、もしくは矛盾なし
            ans[s-1] = c
        else: # 同じ桁に別の条件
            print(-1)
            exit()
    if n > 1 and ans[0] == 0:
        ans[0] = 1
    print(int("".join(map(str,ans))))


if __name__=="__main__":
    main()
