import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

A, B, H, M = inpl()
h = 360 * H / 12 + 30 * M / 60
m = 360 * M / 60
sa = abs(h - m)
sa = min(sa, 360-sa)

print((A*A + B*B - 2*A*B*math.cos(sa*math.pi/180))**0.5)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
