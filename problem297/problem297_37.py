from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import random
#####################################
k=int(input())
if k%2==0:
    print("{:.10f}".format(1/2))
else:
    print("{:.10f}".format((k//2+1)/k))
