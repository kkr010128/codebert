from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import random
#####################################
n=int(input())
A=INPUT()
D=[0]*(n+1)
for i in range(n):
    D[A[i]]=(i+1)
print(*D[1:])
