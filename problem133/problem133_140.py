import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

A, B = map(int, input().split())
print(int(A*B))

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
