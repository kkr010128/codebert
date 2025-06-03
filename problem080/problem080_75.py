import sys
import math
#from queue import *
#import random
#sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

n=inp()

min1=min2=int(1e15)
max1=max2=-int(1e15)

for i in range(n):
	x,y=invr()
	
	min1=min(min1,x+y)
	min2=min(min2,x-y)
	
	max1=max(max1,x+y)
	max2=max(max2,x-y)

ans=max(max1-min1,max2-min2)

print(ans)
