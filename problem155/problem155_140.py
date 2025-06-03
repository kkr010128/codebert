N,M=map(int,input().split())
H=[0]+list(map(int,input().split()))
check=[0]+[1]*N
for _ in range(M):
  a,b=map(int,input().split())
  if H[a]>=H[b]:
    check[b]=0
  if H[b]>=H[a]:
    check[a]=0
print(sum(check))
