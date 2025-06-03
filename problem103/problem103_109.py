import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = inp()
A = inpl()
stk = 0
yen = 1000
for i in range(N):
    if i == 0:
        if A[i] < A[i+1]:
            stk += yen // A[i]
            yen %= A[i]
    elif i == N-1:
        yen += stk * A[i]
    else:
        if A[i-1] <= A[i] and A[i] > A[i+1]:
            yen += A[i]*stk 
            stk = 0
        if A[i-1] >= A[i] and A[i] < A[i+1]:
            stk += yen // A[i]
            yen %= A[i]
print(yen)

# -----------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
