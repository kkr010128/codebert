from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=10**19
###############################################################################\n=17
d,t,s=INPUT()
if d/s<=t:
    print("Yes")
else:
    print("No")
