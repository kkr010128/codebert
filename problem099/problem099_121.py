import sys
import math
import time
sys.setrecursionlimit(int(1e6))
if False:
    dprint = print
else:
    def dprint(*args):
        pass

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
dprint("n, k = ", n, k)

lx = int(0)   # NG
rx = int(1e9) # OK
#ans = 0
while ((rx-lx)>1):
    x = (rx + lx) // 2
    dprint("lx, x, rx = ", lx, x, rx)
    n = 0
    for i in range(len(A)):
        #n += math.ceil(A[i] / x) - 1
        n += (A[i]-1) // x
        if n > k: break
    dprint("n = ", n)
    if n <= k:
        dprint(" smaller x")
        rx = x
    else:
        dprint(" cut less, bigger x")
        lx = x

#ans = math.ceil(rx)
print(rx)
