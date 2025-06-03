import sys
import math
import heapq
from collections import defaultdict, deque
from decimal import *
def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

'''D Anything Goes to zero'''
twoPowM1=[0]*(300000)
twoPowM2=[0]*(300000)
stepsSmall=[0]*(300000)

n=r()
s=input()
bitcount=0
for i in range(n):
    if s[i]=='1':
        bitcount+=1

mod=bitcount-1
if mod>0:
    twoPowM1[0]=1
    for i in range(1,len(twoPowM1)):
        twoPowM1[i]=(twoPowM1[i-1]+twoPowM1[i-1])%mod

mod=bitcount+1
twoPowM2[0]=1
for i in range(1,len(twoPowM2)):
    twoPowM2[i]=(twoPowM2[i-1]+twoPowM2[i-1])%mod

for i in range(1,len(stepsSmall)):
    stepsSmall[i]=1+stepsSmall[i%bin(i).count('1')]

valM1=0;valM2=0
for i in range(n):
    mod=bitcount-1
    if mod>0:
        valM1=((valM1*2)%mod+int(s[i]))%mod
    mod=bitcount+1
    valM2=((valM2*2)%mod+int(s[i]))%mod

for i in range(n):
    pow=n-1-i
    if s[i]=='0':
        mod=bitcount+1
        newVal=(valM2+twoPowM2[pow])%mod
        print(stepsSmall[newVal]+1)
    else:
        mod=bitcount-1
        if mod==0:
            print(0)
        else:
            newVal=(valM1-twoPowM1[pow])%mod
            print(stepsSmall[newVal]+1)