from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import sys
#####################################
n=int(input())
A=INPUT()
s=0
for i in range(n):
    for j in range(i+1,n):
        s+=A[i]*A[j]
print(s)
