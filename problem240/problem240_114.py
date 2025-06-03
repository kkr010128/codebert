import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, M = inpl()
ac = [False] * (N+10)
wa = [0] * (N+10)

a = 0
w = 0
for _ in range(M):
    p, S = input().split()
    p = int(p)
    if S == 'WA':
        if not ac[p]:
            wa[p] += 1
    else:
        if not ac[p]:
            ac[p] = True
            a += 1
            w += wa[p]

print(a, w)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
