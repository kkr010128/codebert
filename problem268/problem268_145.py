import sys
#input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

#import numpy as np

def main():
	n=II()
	A=LI()
	B=[0]*(n+1)
	ans=1
	B[0]=3

	for i in range(n):
		ans*=(B[A[i]])-(B[A[i]+1])
		ans%=10**9+7
		B[A[i]+1]+=1

	print(ans)








if __name__ == "__main__":
	main()
