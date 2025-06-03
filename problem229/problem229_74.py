import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict

# import fractions

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    H, N = il()
    magic = [il() for _ in range(N)]
    dp = [0] * (H + 1)

    dp[0] = 0
    for h in range(1, H + 1):
        for n in range(N):
            if n == 0:
                if magic[n][0] <= h:
                    dp[h] = dp[h - magic[n][0]] + magic[n][1]
                else:
                    dp[h] = magic[n][1]
            else:
                if magic[n][0] <= h:
                    dp[h] = min(dp[h], dp[h - magic[n][0]] + magic[n][1])
                else:
                    dp[h] = min(dp[h], magic[n][1])
    print(dp[-1])


if __name__ == '__main__':
    main()
