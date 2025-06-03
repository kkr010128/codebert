import math
k,n= map(int,input().split())
a = list(map(int,input().split()))
ans = a[0]+k-a[n-1]
for i in range(1,len(a)):
  s = a[i]-a[i-1]
  ans =max(ans,s)
print(k-ans)
