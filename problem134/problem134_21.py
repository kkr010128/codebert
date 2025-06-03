limit=10**18
n=int(input())
A=list(map(int,input().split()))
ans=1
if 0 in A:
  ans=0
else:
  for a in A:
    ans*=a
    if ans > limit:
      ans=-1
      break
print(ans)
