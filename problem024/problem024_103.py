# Aizu Problem ALDS_1_4_D: Allocation
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


def check(n, k, W, p):
    idx = 0
    for i in range(k):
        S = 0
        while W[idx] + S <= p:
            S += W[idx]
            idx += 1
            if idx == n:
                return True
    return False

    
n, k = [int(_) for _ in input().split()]
W = [int(input()) for _ in range(n)]
left, right = 0, 10**16
while right - left > 1:
    mid = (left + right) // 2
    if check(n, k, W, mid):
        right = mid
    else:
        left = mid
print(right)