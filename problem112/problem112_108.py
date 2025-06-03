n,k = map(int,input().split())
A = list(map(int,input().split()))

mod = 10**9 + 7

A.sort(key = lambda x:abs(x),reverse = True)
ans = 1
last = -1
lastp = -1
cnt = 0
for a in A:
    if a >= 0:break
else:
    if k&1:
        for i in range(k):
            ans *= A[n-i-1]
            ans %= mod
    else:
        for i in range(k):
            ans *= A[i]
            ans %= mod
    print(ans)
    exit()
for i in range(k):
    ans *= A[i]
    ans %= mod
    if A[i] < 0:
        last = i
        cnt += 1
    if A[i] > 0:
        lastp = i
if n == k:
    print(ans%mod)
    exit()
if cnt&1:
    first = 0
    firstp = 0
    for a in A[k:]:
        if a > 0 and firstp == 0:
            firstp = a
        if a < 0 and first == 0:
            first = a
    if first == 0 and firstp == 0:
        ans = 0
    elif first == 0 or lastp == -1:
        ans *= pow(A[last],mod-2,mod)*firstp%mod
        ans %= mod
    elif firstp == 0:
        ans *= pow(A[lastp],mod-2,mod)*first%mod
        ans %= mod
    else:
        if A[lastp]*firstp <= A[last]*first:
            ans *= pow(A[lastp],mod-2,mod)*first%mod
            ans %= mod
        else:
            ans *= pow(A[last],mod-2,mod)*firstp%mod
            ans %= mod
print(ans%mod)
