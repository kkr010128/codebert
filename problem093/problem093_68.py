n,k=map(int,input().split())
P=list(map(int,input().split()))
for i in range(n):
  P[i]-=1
C=list(map(int,input().split()))
PP=[0]*n
A=[0]*n
V=[0]*n
for i in range(n):
  if V[i]==1:
    continue
  B=[i]
  c=1
  j=i
  p=C[i]
  while P[j]!=i:
    j=P[j]
    B.append(j)
    c=c+1
    p=p+C[j]
  for j in B:
    A[j]=c
    PP[j]=p
ans=-10**10
for i in range(n):
  if PP[i]<0:
    aans=0
    f=0
  else:
    if k//A[i]-1>0:
      aans=(k//A[i]-1)*PP[i]
      f=1
    else:
      aans=0
      f=2
  l=i
  aaans=-10**10
  if f==0:
    for j in range(min(k,A[i])):
      aans=aans+C[P[l]]
      l=P[l]
      if aans>aaans:
        aaans=aans
  elif f==1:
    for j in range(k%A[i]+A[i]):
      aans=aans+C[P[l]]
      l=P[l]
      if aans>aaans:
        aaans=aans
  else:
    for j in range(min(k,2*A[i])):
      aans=aans+C[P[l]]
      l=P[l]
      if aans>aaans:
        aaans=aans
  if aaans>ans:
    ans=aaans
print(ans)