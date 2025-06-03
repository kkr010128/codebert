import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, M = inpl()
H = inpl()
dp = [True] * N
for _ in range(M):
    A, B = inpl()
    if H[A-1] > H[B-1]:
        dp[B-1] = False
    elif H[A-1] < H[B-1]:
        dp[A-1] = False
    else:
        dp[A-1] = False
        dp[B-1] = False
ans = 0
for i in dp:
    if i:
        ans += 1
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
