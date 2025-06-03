N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
ok = 10**12
ng = -1


def check(time):
    shugyou = 0
    for i in range(N):
        if A[i]*F[i] > time:
            shugyou += A[i] - (time//F[i])
    return shugyou <= K


while ok - ng > 1:
    mid = (ok + ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
