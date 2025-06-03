import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

A, B = map(int, input().split())
print(A*B // math.gcd(A,B))

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
