from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import sys
#####################################
a,b=INPUT()
if a>=2*b:
    print(a-2*b)
else:
    print(0)
