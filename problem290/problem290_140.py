def f(point):
    k = K
    for i in range(N):
        a = A[i]
        f = F[i]
        if a*f > point:
            k -= a - point//f
        if k < 0:
            return False
    # print(point, k)
    return True

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
l = -1
r = 10**18+1
while (r-l) > 1:
    mid = (r+l)//2
    if f(mid):
        r = mid
    else:
        l = mid
print(r)
