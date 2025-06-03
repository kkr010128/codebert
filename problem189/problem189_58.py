N=list(map(int,input().split()))
ans=0
for x in range(2):
  if N[x]==0 or N[x]==1:
    pass
  else:
    ans += N[x]*(N[x]-1)/2
print(int(ans))