import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(input())

mn = 1001001001001
a = 1
while a*a <= N:
    if N % a == 0:
        mn = min(mn, a + N//a - 2)
    a += 1
print(mn)
    

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
