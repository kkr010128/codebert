N, K = (int(x) for x in input().split())
check=[False]*N
ans=N
for i in range(K):
  d=int(input())
  A=list(map(int, input().split()))
  for j in range(d):
    if check[A[j]-1]==False:
      ans-=1
      check[A[j]-1]=True
print(ans)