import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque
import copy

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def req_count(P, K, W):
    cnt = 0
    for k in range(K):
        p = 0
        while p + W[cnt] <= P:
            p += W[cnt]
            cnt += 1
            if cnt == len(W):
                return cnt
    else:
        return cnt


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, K = il()
    W = [ii() for _ in range(N)]

    left, right = 0, sum(W)
    while right - left != 1:
        middle = (left + right) // 2
        n = req_count(middle, K, W)
        if n >= N:
            right = middle
        else:
            left = middle
    print(right)


if __name__ == '__main__':
    main()

