def oginau(k):
  if len(k)!=N:
    k=str(("0"*(N-len(k)))+k)
    return k
  else:
    return k
N,M,X=map(int,input().split())
L=[[] for i in range(N)]
for i in range(N):
  L1=list(map(int,input().split()))
  L[i]=L1
mina=10**10
for i in range(2**N):
  R=[0 for i in range(M)]
  money=0
  s=str(bin(i)[2:])
  s=oginau(s)
  for j in range(N):
    if s[j]=="1":
      money+=L[j][0]
      for w in range(1,M+1):
        R[w-1]+=L[j][w]
  if len([i for i in R if i>=X])==M:
    mina=min(money,mina)
if mina==10**10:
  print(-1)
else:
  print(mina)