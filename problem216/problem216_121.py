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

A = inpl()
A.sort()
if A[0]!=A[2]:
    if A[0]==A[1]:
        print('Yes')
        sys.exit()
    if A[1]==A[2]:
        print('Yes')
        sys.exit()
print('No')


# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)