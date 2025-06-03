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

N = inp()
A = inpl()
A.sort()
dp = [False] * 1001001
nt = -1

for i in A:
    if i != nt:
        dp[i] = True
    else:
        dp[i] = False
    nt = i

ans = 0
mx = A[N-1]
nt = -1
for i in A:
    if dp[i]:
        ans += 1
    if i == nt:
        continue
    nt = i
    j = i
    while j <= mx:
        dp[j] = False
        j += i

print(ans)

# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)