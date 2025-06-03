MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from bisect import bisect_left,bisect_right
from collections import deque

    
def main():
    n,k = map(int,input().split())
    ans = 0
    G = [0] * (1 + k)
    for g in range(k,0,-1):
        ret = pow((k//g),n,MOD)
        for j in range(2 * g,k + 1,g):
            ret -= G[j]
        G[g] = ret
        ans += ret * g
        ans %= MOD
    
    print(ans) 

if __name__ =='__main__':
    main()  