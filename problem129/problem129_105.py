n=int(input())
a=[int(x) for x in input().rstrip().split()]
a.sort()
ma=max(a)
dp=[0]*ma
for i in a:
  dp[i-1]+=1

l=[0]*ma
ans=0
for i in a:
  j=i
  if l[i-1]==0 and dp[i-1]==1:
    ans+=1
  while(j<=ma):
    l[j-1]+=1
    if j+i<=ma:
      j+=i
    else:
      break
print(ans)
