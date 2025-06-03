from random import *
D=int(input())
C=list(map(int,input().split()))
S=[list(map(int,input().split())) for i in range(D)]
X=[0]*26
XX=[0]*26
P=[]
Y,Z=0,0
V,W=0,0
T,U=0,0
for i in range(D):
  for j in range(26):
    X[j]+=C[j]
    XX[j]+=X[j]
  Y,Z=-1,-10**20
  V,W=Y,Z
  T,U=V,W
  for j in range(26):
    if Y==-1:
      Y,Z=0,X[0]+S[i][0]
      continue
    if Z<X[j]+S[i][j]:
      T,U=V,W
      V,W=Y,Z
      Y,Z=j,X[j]+S[i][j]
    elif W<X[j]+S[i][j]:
      T,U=V,W
      V,W=j,X[j]+S[i][j]
    elif U<X[j]+S[i][j]:
      T,U=j,X[j]+S[i][j]
  XX[Y]-=X[Y]
  X[Y]=0
  P.append([Y,V,T])
  if randrange(0,50)==0:
    P[i][1]=randrange(0,26)
  if randrange(0,5)==0:
    P[i][2]=randrange(0,26)
  P[i]=tuple(P[i])
SCORE=0
X=[0]*26
for i in range(D):
  SCORE+=S[i][P[i][0]]
  for j in range(26):
    X[j]+=C[j]
  X[P[i][0]]=0
  SCORE-=sum(X)
SCORE2=0
YY=[]
for i in range(D):
  for k in range(2):
    d,q=i,P[i][k+1]
    SCORE2=SCORE
    YY=XX[:]
    SCORE2-=S[d][P[d][0]]
    SCORE2+=S[d][q]
    for j in range(26):
      X[j]=0
    YY[P[d][0]],YY[q]=0,0
    for j in range(D):
      if j==d:
        Z=q
      else:
        Z=P[j][0]
      X[P[d][0]]+=C[P[d][0]]
      X[q]+=C[q]
      X[Z]=0
      YY[P[d][0]]+=X[P[d][0]]
      YY[q]+=X[q]
    if SCORE2-sum(YY)>SCORE-sum(XX):
      z=[P[i][k+1]]
      for l in range(3):
        if l!=k:
          z.append(P[i][l])
      P[i]=tuple(z)
      XX=YY[:]
      SCORE=SCORE2
for i in range(D):
  print(P[i][0]+1)