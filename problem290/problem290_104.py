import sys
import math
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
F = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
A = A[::-1]
F.sort()

def test(x):
    res = 0
    for i in range(N):
        t = A[i] * F[i]
        if t > x:
            res += math.ceil((t - x) / F[i])
    
    return res <= K

ng = -1
ok = 10**18

while ng + 1 < ok:
    mid = (ng + ok) // 2
    if test(mid):
        ok = mid
    else:
        ng = mid
print(ok)