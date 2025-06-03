import math

N=int(input())
A=list(map(int,input().split()))

a=max(A)
def era(n):
  prime=[]
  furui=list(range(2,n+1))
  while furui[0]<math.sqrt(n):
    prime.append(furui[0])
    furui=[i for i in furui if i%furui[0]!=0]
  return prime+furui

b=A[0]
for i in range(1,N):
  b=math.gcd(b,A[i])

if b!=1:
  print("not coprime")
  exit()

furui=era(10**6+7)
minfac=list(range(10**6+7))
for i in furui:
  for j in range(i,(10**6+7)//i):
    if minfac[i*j]==i*j:
      minfac[i*j]=i
      
dummy=[False]*(10**6+7)
for i in range(N):
  k=A[i]
  while k!=1:
    if dummy[minfac[k]]==True:
      print("setwise coprime")
      exit()
    else:
      dummy[minfac[k]]=True
      f=minfac[k]
      while k%f==0:
        k//=f
print("pairwise coprime")