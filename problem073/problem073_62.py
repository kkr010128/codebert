from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
########################################################
F=[1]*(10**6+1)
for i in range(2,10**6+1):
    for j in range(i,10**6+1,i):
        F[j]+=1
ans=0
n=int(input())
for c in range(1,n):
    ans+=F[n-c]
print(ans)
