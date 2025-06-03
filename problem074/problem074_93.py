mod=998244353
N,K=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(K)]

S=[0 for _ in range(N+1)]
S[1]=1
for i in range(1,N):
  S[i+1]=S[i]
  for l,r in A:
    S[i+1]+=S[max(0,i-l+1)]-S[max(0,i-r)]
  S[i+1]%=mod
print((S[N]-S[N-1])%mod)