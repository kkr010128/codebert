import math

INF=float('inf')
ans1='pairwise coprime'
ans2='setwise coprime'
ans3='not coprime'

n=int(input())
A=list(map(int,input().split()))

P=[0]*(10**6+1)
for i in A:
  P[i]+=1

pairwise=True
for i in range(2,10**6+1):
  cnt=0
  for j in range(i,10**6+1,i):
    cnt+=P[j]
  if cnt>1:
    pairwise=False
    break

if pairwise:
  print(ans1)
  exit()
  
g=math.gcd(A[0],A[1])
for i in A:
  g=math.gcd(g,i)

if g==1:
  print(ans2)
else:
  print(ans3)