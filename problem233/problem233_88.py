n=int(input())
p=list(map(int,input().split()))
min_val=10**18
ans=0
for i in range(n):
  if i==0:
    min_val=p[i]
    ans+=1
    continue
  if min_val>=p[i]:
    min_val=p[i]
    ans+=1
print(ans)


