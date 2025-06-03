N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)
mod=10**9+7
inv_t=[0,1]
factorial=[1,1]
factorial_re=[1,1]
for i in range(2,N+1):
    inv_t.append(inv_t[mod%i]*(mod-mod//i)%mod)
for i in range(2,N+1):
    factorial.append(factorial[i-1]*i%mod)
    factorial_re.append(factorial_re[i-1]*inv_t[i]%mod)

ans=0
for i in range(N-K+1):
    if i==N-K:
        ans+=A[i]
        ans%=mod
        break
    ans+=A[i]*factorial[N-1-i]*factorial_re[K-1]*factorial_re[N-K-i]%mod
    ans%=mod
for i in range(N-K+1):
    if i==N-K:
        ans-=A[N-i-1]
        ans%=mod
        break
    ans-=A[N-i-1]*factorial[N-1-i]*factorial_re[K-1]*factorial_re[N-K-i]%mod
    ans%=mod
print(ans)
