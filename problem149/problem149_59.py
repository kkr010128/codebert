N, M, X = map(int, input().split())
C=[]
A=[]
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans=10**5*N+1
for maskN in range(1<<N):
  cost=0
  level=[0]*M
  for n in range(N):
    if (maskN>>n&1):
      cost+=C[n]
      for m in range(M):
        level[m] += A[n][m]
  for l in level:
    if l < X:
      break
  else:
    ans=min(ans, cost)
print(f'{ans if ans!=10**5*N+1 else "-1"}')
