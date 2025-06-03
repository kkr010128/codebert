import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SI(): return input().split()

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import ceil, floor, log2
from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product


def solve():
    n = II()
    A = LI()

    memo = {}
    ans = 0
    for i in range(n):
        mae = (i+1) + A[i]
        ima = (i+1) - A[i]
        ans += memo.get(ima, 0)
        memo[mae] = memo.get(mae, 0) + 1
    # print(memo)
    print(ans)


if __name__ == '__main__':
    solve()
