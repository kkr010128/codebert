import math
n = int(input())
ans=0
k = [[0]*10 for i in range(10)]

for i in range(1,n+1):
  j = str(i)
  l = int(j[0])
  r = int(j[-1])
  k[l][r]+=1
  
for i in range(10):
  for j in range(10):
    if i==0 or j==0:
      continue
    if i==j:
      ans += k[i][j]*k[i][j]
    else:
      ans += k[i][j]*k[j][i]
print(ans)