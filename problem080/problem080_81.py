import sys
#from collections import deque
#from functools import *
#from fractions import Fraction as f
from copy import *
from bisect import *	
#from heapq import *
#from math import ceil
#from itertools import permutations ,product
 
def eprint(*args):
    print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('all.txt','w')
di=[[-1,0],[1,0],[0,1],[0,-1]]
def inc(d,c,x=1):
	d[c]=d[c]+x if c in d else x
def bo(i):
	return ord(i)-ord('A')	
def li():
	return [int(xx) for xx in input().split()]
def fli():
	return [float(x) for x in input().split()]	
def comp(a,b):
	if(a>b):
		return 2
	return 2 if a==b else 0		
def gi():	
	return [xx for xx in input().split()]
def fi():
	return int(input())
def pro(a): 
	return reduce(lambda a,b:a*b,a)		
def swap(a,i,j): 
	a[i],a[j]=a[j],a[i]	
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())			
def gh():
	sys.stdout.flush()
def isvalid(i,j):
	return 0<=i<n and 0<=j<m and a[i][j]!="."
def bo(i):
	return ord(i)-ord('a')	
def graph(n,m):
	for i in range(m):
		x,y=mi()
		a[x].append(y)
		a[y].append(x)
mod=10**9+7
t=1
while t>0:
	t-=1
	n=fi()
	a=[]
	b=[]
	for i in range(n):
		x,y=mi()
		a.append(x+y)
		b.append(x-y)
	p=max(a)-min(a)
	q=max(b)-min(b)
	print(max(p,q))	
		

