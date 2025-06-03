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
        a,b,c=In()
        k=I()
        t1,t2=0,0
        if a>=b:
            t1=0
            while b<=a:
                b*=2
                t1+=1
        if b>=c:
            t2=0
            while c<=b:
                c*=2
                t2+=1

        #print(a,b,c)
        if a<b and b<c:
            if t1+t2<=k:
                print('Yes')
            else:
                print('No')
        else:
            print('No')

    except:
        pass
        
M = 998244353
P = 1000000007
 
if __name__ == '__main__':
    #for _ in range(I()):main()
    for _ in range(1):main()


