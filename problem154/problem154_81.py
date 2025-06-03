import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
start_time = time.perf_counter()
# ------------------------------

N, K = inpl()
dp = [False] * N
for i in range(K):
    d = inp()
    A = inpl()
    for a in A:
        dp[a-1] = True
cnt = 0
for bl in dp:
    if not bl:
        cnt += 1
print(cnt)

# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)