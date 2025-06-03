import sys

input=sys.stdin.buffer.readline


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


def main():
	n=II()
	XY=[LI() for _ in range(n)]
	
	A=[]
	B=[]
	for x,y in XY:
		A.append(x+y)
		B.append(x-y)
	
	A.sort()
	B.sort()
	a=A[-1]-A[0]
	b=B[-1]-B[0]
	
	print(max(a,b))










if __name__=="__main__":
	main()
