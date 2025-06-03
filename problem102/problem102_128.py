import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, K = inpl()
A = inpl()
for i in range(K, N):
    if A[i] > A[i-K]:
        print('Yes')
    else:
        print('No')

# -----------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
