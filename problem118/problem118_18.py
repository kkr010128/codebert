import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(read())
ans = 0
for i in range(1, N+1):
    n = N // i
    ans += 0.5 * n * (2*i + i * (n-1))
print(int(ans))

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
