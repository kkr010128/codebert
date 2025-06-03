n=int(input())
an=[int(i) for i in input().split()]
ans=1
for a in an:
  ans*=a
  if ans>10**18:
    ans=-1
    break
    
if 0 in an:
  ans=0
print(ans)