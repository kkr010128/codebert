import sys
input = sys.stdin.readline
H,W,K=map(int,input().split())
CO=[[0 for i in [0]*W] for j in [0]*H]
DO=[[0 for i in [0]*W] for j in [0]*H]
for i in range(H):
 C=input()
 for j in range(W):
  DO[i][j]=int(C[j])
CO[H-1]=DO[H-1]
F=1000000
for s in range(2**(H-1)):
 D=0
 E=0
 Sui=[0]*(H-1)
 for t in range(H-1):
  if ((s >> t) & 1):
   Sui[t]+=1
 for m in range(H-1):
  E+=Sui[m]
 for k in range(H-1):
  if Sui[k]==0:
   for i in range(W):
    CO[H-k-2][i]=DO[H-k-2][i]+CO[H-k-1][i]
  else:
   for i in range(W):
    CO[H-k-2][i]=DO[H-k-2][i]
 lst=[0]*H
 for h in range(W):
  c=max(CO[x][h] for x in range(H))
  d=max(lst[y]+CO[y][h] for y in range(H))
  if c>K:
   E=1000000
   break
  elif d>K:
   D+=1
   lst=[0]*H
  for z in range(H):
   lst[z]+=CO[z][h]
 F=min(F,D+E)
print(F)