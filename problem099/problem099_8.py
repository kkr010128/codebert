n,k = map(int,input().split())
L = list(map(int,input().split()))
ok = 0
ng = 10**9
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    cur = 0
    for i in range(n):
        cur += L[i]//mid
    if cur > k:
        ok = mid
    elif cur <= k:
        ng = mid
K = [mid-1, mid, mid+1]
P = []
for i in range(3):
    res = 0
    if K[i] > 0:
        for j in range(n):
            res += (L[j]-1)//K[i]
        if res <= k:
            P.append(K[i])
print(min(P))
