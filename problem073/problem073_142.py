import math
N=int(input())

def era(n):
  prime=[]
  furui=list(range(2,n+1))
  while furui[0]<math.sqrt(n):
    prime.append(furui[0])
    furui=[i for i in furui if i%furui[0]!=0]
  return prime+furui

furui=era(10**6+7)
minfac=list(range(10**6+8))
for i in furui:
  for j in range(i,(10**6+7)//i+1):
    if minfac[i*j]==i*j:
      minfac[i*j]=i

ans=0   
for i in range(1,N):
  temp=1
  temp2=1
  l=1
  while i != 1:
    if minfac[i]!=l:
      temp*=temp2
      temp2=2
    else:
      temp2+=1
    l=minfac[i]
    i//=l
  temp*=temp2
  ans+=temp
print(ans)