N=int(input())
X=[int(x) for x in input().split()]

ans=10**9
for p in range(-200, 200):
  ref=0
  for x in X:
    ref+=(x-p)**2
  #print(ref)
  ans=min(ans, ref)
  
print(ans)