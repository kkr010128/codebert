N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

def check(mid):
    cnt = 0
    for i in range(N):
        tmp = mid // F[i]
        cnt += max(A[i] - tmp, 0)
    return cnt <= K

check(2)

l, r = -1, 10**30
while r-l > 1:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid

print(r)
