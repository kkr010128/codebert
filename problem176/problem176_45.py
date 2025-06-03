import sys
input = sys.stdin.buffer.readline

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from itertools import combinations, permutations
from itertools import accumulate
from math import ceil, sqrt, pi

MOD = 10 ** 9 + 7
INF = 10 ** 18

def divisors(n) -> list:
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res


N, K = map(int, input().split())
MOD = 10 ** 9 + 7

cnt = defaultdict(int)
for k in range(1, K + 1):
    for d in divisors(k):
        cnt[d] += 1
#print(cnt)

tmp = defaultdict(int)
for k in range(K, 0, -1):
    tmp[k] = pow(cnt[k], N, MOD)
    for i in range(2, K // k + 1):
        tmp[k] -= tmp[i * k]
#print(tmp)

ans = 0
for k in range(1, K + 1):
    ans = (ans + k * tmp[k]) % MOD
print(ans)