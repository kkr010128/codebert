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


def main():
	n=II()
	A=[]
	B=[]
	for _ in range(n):
		a,b=MI()
		A.append(a)
		B.append(b)
	A.sort()
	B.sort()
	#print(A,B)

	r=n//2
	l=(n-1)//2
	#print(l,r)

	mi=A[l]+A[r]
	ma=B[l]+B[r]

	ans=(ma-mi)-(ma-mi)*(n%2)//2+1
	print(ans)







if __name__ == "__main__":
	main()
