from random import *
D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(D)]
X=[0]*26
XX=[0]*26
P=[]
for i in range(D):
  for j in range(26):
    X[j]+=C[j]
    XX[j]+=X[j]
  P.append([])
  for j in range(26):
    P[i].append(j)
  P[i].sort(reverse=True,key=lambda x:X[x]+S[i][x])
  XX[P[i][0]]-=X[P[i][0]]
  X[P[i][0]]=0
SC,SC2=0,0
for i in range(D):
  SC+=S[i][P[i][0]]
YY=[]
Y=[]
for l in range(25):
  for k in range(25):
    for i in range(D):
      SC2=SC
      YY=XX[:]
      Y=X[:]
      SC2-=S[i][P[i][0]]
      SC2+=S[i][P[i][k+1]]
      for j in range(26):
        Y[j]=0
      YY[P[i][0]],YY[P[i][k+1]]=0,0
      for j in range(D):
        if j==i:
          Z=P[j][k+1]
        else:
          Z=P[j][0]
        Y[P[i][0]]+=C[P[i][0]]
        Y[P[i][k+1]]+=C[P[i][k+1]]
        Y[Z]=0
        YY[P[i][0]]+=Y[P[i][0]]
        YY[P[i][k+1]]+=Y[P[i][k+1]]
      if SC2-sum(YY)>SC-sum(XX):
        P[i].insert(0,P[i][k+1])
        del P[i][k+2]
        XX=YY[:]
        SC=SC2
for i in range(D):
  print(P[i][0]+1)