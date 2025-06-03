N,K=map(int,input().split())
A=list(map(int,input().split()))
imos=[0 for i in range(N+1)]
zero=[0 for i in range(N+1)]
ANS=[str(N)]*N
if K>=40:
  ans=" ".join(ANS)
  print(ans)
else:
  for t in range(K):
    for i in range(N):
      l=max(0,i-A[i])
      r=min(N,i+A[i]+1)
      imos[l]+=1
      imos[r]-=1
    for i in range(0,N):
      imos[i+1]+=imos[i]
      A[i]=imos[i]
    imos=[0 for i in range(N+1)]
  for i in range(N):
    A[i]=str(A[i])
  ans=" ".join(A)
  print(ans)  