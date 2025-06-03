n=int(input())
x=list(map(int,input().split()))
ans=10**9
for i in range(1,101):
  tmp=0
  for j in range(n):
    tmp+=(i-x[j])*(i-x[j])
  ans=min(ans,tmp)
print(ans)