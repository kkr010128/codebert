import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)

def solve(X):
    s = 0
    for i in range(N):
        if A[i]*F[i]>X:
            s += math.ceil((A[i]*F[i]-X)/F[i])
    # print(X, s)
    return s <= K

if sum(A) <= K:
    print(0)
else:
    l, r = 0, 10**12+10
    while l+1<r:
        mid = (l+r)//2
        if solve(mid):
            r = mid
        else:
            l = mid
    print(r)