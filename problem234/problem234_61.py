from math import factorial
n=int(input())
d=[[0]*10 for _ in range(10)]
for i in range(1,n+1):
  j=i
  while True:
    if j//10:j//=10
    else:break
  d[j][i%10]+=1
ans=0
for i in range(10):
  for j in range(10):
    ans+=d[i][j]*d[j][i]
print(ans)