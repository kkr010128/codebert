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

n, a, b = inpl()
l = n // (a + b)
m = n % (a + b)
print(a * l + min(m, a))

# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)