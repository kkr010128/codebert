from time import *
from random import *
t=time()
T0,T1=2000,600
Tt=2000
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
A,B=0,0
e=0
E=1
for i in range(50):
  e+=E
  E*=1/(i+1)
def f(x):
  global e,Tt
  if x>=0:
    return True
  else:
    return randrange(0,10000000)<=pow(e,x/Tt)
for l in range(8):
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
      if f((SC2-sum(YY))-(SC-sum(XX))):
        P[i].insert(0,P[i][k+1])
        del P[i][k+2]
        XX=YY[:]
        SC=SC2
    for i in range(1,D-1):
      SC2=SC
      YY=XX[:]
      Y=X[:]
      A=i
      B=randrange(A+1,D)
      SC2-=S[A][P[A][0]]+S[B][P[B][0]]
      SC2+=S[A][P[B][0]]+S[B][P[A][0]]
      for j in range(26):
        Y[j]=0
      YY[P[A][0]],YY[P[B][0]]=0,0
      for j in range(D):
        if j==A:
          Z=P[B][0]
        elif j==B:
          Z=P[A][0]
        else:
          Z=P[j][0]
        Y[P[A][0]]+=C[P[A][0]]
        Y[P[B][0]]+=C[P[B][0]]
        Y[Z]=0
        YY[P[A][0]]+=Y[P[A][0]]
        YY[P[B][0]]+=Y[P[B][0]]
      if f((SC2-sum(YY))-(SC-sum(XX))):
        P[A],P[B]=P[B][:],P[A][:]
        XX=YY[:]
        SC=SC2
      if k&1:
        continue
      B=randrange(0,A)
      SC2-=S[A][P[A][0]]+S[B][P[B][0]]
      SC2+=S[A][P[B][0]]+S[B][P[A][0]]
      for j in range(26):
        Y[j]=0
      YY[P[A][0]],YY[P[B][0]]=0,0
      for j in range(D):
        if j==A:
          Z=P[B][0]
        elif j==B:
          Z=P[A][0]
        else:
          Z=P[j][0]
        Y[P[A][0]]+=C[P[A][0]]
        Y[P[B][0]]+=C[P[B][0]]
        Y[Z]=0
        YY[P[A][0]]+=Y[P[A][0]]
        YY[P[B][0]]+=Y[P[B][0]]
      if f((SC2-sum(YY))-(SC-sum(XX))):
        P[A],P[B]=P[B][:],P[A][:]
        XX=YY[:]
        SC=SC2
    Tt=pow(T0,1-(time()-t))*pow(T1,time()-t)
'''
X=[0]*26
SC=0
for i in range(D):
  for j in range(26):
    X[j]+=C[j]
  X[P[i][0]]=0
  SC-=sum(X)
  SC+=S[i][P[i][0]]
print(SC)
'''
for i in range(D):
  print(P[i][0]+1)