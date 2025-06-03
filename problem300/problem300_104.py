from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import random
#####################################
a,b=INPUT()
A=min(a,b)
B=max(a,b)
X=[]
P=[]
for i in range(1,int(M.sqrt(A)+1)):
    if A%i==0:
        if A//i==i:
            P.append(i)
        else:
            P.append(i)
            P.append(A//i)
Q=[]

for i in range(1,int(M.sqrt(B)+1)):
    if B%i==0:
        if B//i==i:
            Q.append(i)
        else:
            Q.append(i)
            Q.append(B//i)
X=list(set(P)&set(Q))
X.sort()
ans=0
#sprint(X)
bool=[True]*len(X)
for i in range(len(X)):
    if X[i]!=1 and bool[i]==True:
        ele=X[i]
        for j in range(i+1,len(X)):
            if X[j]%ele==0:
                bool[j]=False

for i in range(len(X)):
    if bool[i]==True:
        ans+=1

print(ans)
