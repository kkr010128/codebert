from math import sqrt
n=int(input())
ans=float('inf')
for i in range(1,int(sqrt(n))+1):
  if n%i==0:
    res=i+n//i-2
    ans=min(ans,res)
print(ans)