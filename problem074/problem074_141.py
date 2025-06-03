from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=998244353
########################################################
n,k=INPUT()
A=[]
for i in range(k):
    x,y=INPUT()
    A.append([x,y])
A.sort()
s,e=-1,-1
S=[]
for i in range(len(A)):
    if i==0:
        S.append([A[i][0],A[i][1]])
    else:
        if A[i][0]>S[-1][1]:
            S.append([A[i][0],A[i][1]])
        else:
            S[-1][1]=A[i][1]
cum=[0]*(n+1)
dp=[0]*(n+1)
dp[1]=1
cum[1]=1
for i in range(2,n+1):
    for ele in S:
        x=ele[0]
        y=ele[1]
        dp[i]=(dp[i]+cum[max(i-x,0)]-cum[max(0,i-y-1)])%J
    cum[i]=(cum[i-1]+dp[i])%J
print(dp[n])
