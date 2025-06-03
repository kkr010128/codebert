from sys import stdin, stdout
import math,sys,heapq
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict
from os import path
import bisect as bi
def yes():print('YES')
def no():print('NO')
if (path.exists('input.txt')): 
    #------------------Sublime--------------------------------------#
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
    def I():return (int(input()))
    def In():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def I():return (int(stdin.readline()))
    def In():return(map(int,stdin.readline().split()))

def dict(a):
    d={}
    for x in a:
        if d.get(x,-1)!=-1:
            d[x]+=1
        else:
            d[x]=1
    return d

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bi.bisect_right(a, x)
    if i != len(a):
        return i
    else:            
        return -1

def main():
    try:
        n=I()
        if n<=599:print(8)
        elif n<=799:print(7)
        elif n<=999:print(6)
        elif n<=1199:print(5)
        elif n<=1399:print(4)
        elif n<=1599:print(3)
        elif n<=1799:print(2)
        elif n<=1999:print(1)



    except:
        pass
        
M = 998244353
P = 1000000007
 
if __name__ == '__main__':
    #for _ in range(I()):main()
    for _ in range(1):main()


