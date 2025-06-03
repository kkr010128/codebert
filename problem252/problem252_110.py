import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from bisect import bisect_left
def resolve():
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()

    def count(x): # the number of (i, j)s s.t. A[i] + A[j] >= x
        res = 0
        for a in A:
            idx = bisect_left(A, x - a)
            res += n - idx
        return res

    left = 0
    right = 200001
    while right - left > 1:
        mid = (left + right) // 2
        if count(mid) < m:
            right = mid
        else:
            left = mid

    x = right
    res = 0
    for a in A:
        idx = bisect_left(A, x - a)
        res += 2 * a * (n - idx)
    res += (x - 1) * (m - count(x))
    print(res)
resolve()