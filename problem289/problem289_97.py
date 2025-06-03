import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')

#2325
#import numpy as np
import math

def main():
	a,b,x=MI()

	k=0

	if b/2<=x/a**2:
		k=2/a*(b-x/a**2)
	else:
		k=a*b**2/(2*x)

	print(math.degrees(math.atan(k)))





if __name__ == "__main__":
	main()