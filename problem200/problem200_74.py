from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    A,B,M = map(int, input().split())
    v1 =list(map(int, input().split())) 
    v2 =list(map(int, input().split())) 
    res = INF
    for i in range(M):
        X,Y,C = map(int, input().split())
        res = min(res,v1[X-1] + v2[Y-1] - C)

    res = min(res,min(v1) + min(v2))
    res = max(0,res)
    print(res)


if __name__ == '__main__':
    solve()
