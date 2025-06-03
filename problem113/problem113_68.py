#-------------------------------------------------------------------------------
#関数定義
def f(a,d,T):
    try:
        return T[d+1:].index(a)+(d+1)
    except ValueError:
        return len(T)

def g(a,d,T):
    try:
        return (d-1)-T[d-1::-1].index(a)
    except ValueError:
        return 0
#-------------------------------------------------------------------------------
#インポート
from math import inf,exp
from random import random,randint
import time
from copy import copy
#-------------------------------------------------------------------------------
#定数
TIME_LIMIT=1.864 #ループの時間制限  
A=26 #アルファベットの数
START=time.time()

ALPHA=15
ep=10**(-6) #アニーリングの微小温度
#-------------------------------------------------------------------------------
#読み込み部
D=int(input())

C=[True]+list(map(int,input().split())) #減る満足度のベース
S=[True]*(D+1) #S[d][i] :(d+1)日目にコンテストiを開催した時の満足度

for i in range(1,D+1):
    S[i]=[0]+list(map(int,input().split()))           
#-------------------------------------------------------------------------------
#貪欲部
L=[0]*(A+1)
T=[0]
for d in range(1,D+1):
    Y=-inf
    E=0
    for a in range(1,A+1):
        X=S[d][a]
        for s in range(1,A+1):
            if a!=s:
                X-=C[s]*(d-L[s])

        if X>Y:
            Y=X
            E=a
    L[E]=d
    T.append(E)
#-------------------------------------------------------------------------------
#調節部
t=time.time()-START
while t<TIME_LIMIT:
    d=randint(1,D)
    p=T[d]
    q=randint(1,A)

    Delta=(S[d][q]-S[d][p])+(d-g(q,d,T))*(f(q,d,T)-d)*C[q]-(d-g(p,d,T))*(f(p,d,T)-d)*C[p]
    if (Delta>=0) or (Delta<0 and random()<exp(Delta/(ALPHA*(TIME_LIMIT-t)+ep))):
        T[d]=q
    
    t=time.time()-START

for i in range(1,D+1):
    print(T[i])
