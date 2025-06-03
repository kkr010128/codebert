import bisect
import sys
from bisect import bisect_left
from operator import itemgetter

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]

def main():
    N = ii()
    L = lmi()
    L.sort()
    # print(L)
    # 2辺を固定して、2辺の和より長い辺の数を数える
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            limit = L[i] + L[j]
            longer = bisect_left(L, limit)
            tmp = longer - (j + 1)
            # print(limit, longer, tmp)
            count += longer - (j + 1)

    print(count)
    return

main()
