N,M,X=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(N)]
inf=(10**5)*12+1
ans=inf
for i in range(1,2**N):
  tmp=[0]*M
  c=0
  for j in range(N):
    if i>>j&1:
      for k in range(M):
        tmp[k]+=B[j][k+1]
      c+=B[j][0]
  if len([i for i in tmp if i>=X])==M:
    ans=min(c,ans)
print(ans if ans<inf else -1)