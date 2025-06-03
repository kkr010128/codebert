import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import numpy as np

def main():
	n=II()
	A=LI()

	A=np.array(A)

	B=np.cumsum(A)
	C=np.cumsum(A[::-1])

	#print(B,C)

	D=abs(B[:-1]-C[:-1][::-1])
	#print(D)

	print(np.min(D))









if __name__ == "__main__":
	main()
