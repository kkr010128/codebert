MOD = 10**9+7
N,K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse = True)
ans = 1
if A[-1] >= 0:
    for i in range(K):
        ans *= A[i]
        ans %= MOD
elif A[0] < 0:
    if K % 2 == 0:
        for i in range(K):
            ans *= A[N-1-i]
            ans %= MOD
    else:
        for i in range(K):
            ans *= A[i]
            ans %= MOD
else:
    r,l = N-1,0
    n = 0
    while n < K:
        if K-n == 1:
            ans *= A[l]
            ans %= MOD
            n += 1
        else:
            if A[r]*A[r-1] > A[l]*A[l+1]:
                ans *= (A[r]*A[r-1])
                ans %= MOD
                r -= 2
                n += 2
            else:
                ans *= A[l]
                ans %= MOD
                l += 1
                n += 1
print(ans)
