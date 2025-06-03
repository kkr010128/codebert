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

import bisect

def main():
	n,a,b=MI()

	if abs(b-a)%2==0:
		ans=abs(b-a)//2

	else:
		if b<a:
			a,b=b,a
		ans=min(a-1,n-b)+1+(b-a-1)//2

	print(ans)

















if __name__ == "__main__":
	main()
