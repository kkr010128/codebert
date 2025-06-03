N,K=map(int, input().split())
P=998244353
S=[tuple(map(int,input().split())) for _ in range(K)]

f=[0]*(10**6)
f[0]=1
for i in range(N):
  for l, r in S:
    f[i+l] += f[i]
    f[i+l]%=P
    f[i+r+1]-=f[i]
    f[i+r+1]%=P
  if i:
    f[i+1]+=f[i]
  f[i]%=P
print(f[N-1])