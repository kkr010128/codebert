import sys,math,collections
from collections import defaultdict

#from itertools import permutations,combinations
	
def file():
	sys.stdin = open('input.py', 'r')
	sys.stdout = open('output.py', 'w') 
def get_array():
	l=list(map(int, input().split()))
	return l
def get_2_ints():	
	a,b=map(int, input().split())
	return a,b
def get_3_ints():	
	a,b,c=map(int, input().split())
	return a,b,c	
def sod(n):
	n,c=str(n),0
	for i in n:	
		c+=int(i)
	return c	

def getFloor(A, x):

	(left, right) = (0, len(A) - 1)

	floor = -1
	while left <= right:
		mid = (left + right) // 2
		if A[mid] == x:
			return A[mid]
		elif x < A[mid]:
			right = mid - 1
		else:
			floor = A[mid]
			left = mid + 1
			
	return floor
#file()	
def main():
	l,r,n=get_3_ints()
	c=0
	for i in range(min(l,r),max(l,r)+1):
		#print(i)
		if(i%n==0):
			c+=1
	print(c)		


                       

















				

			







            
			
































		








if __name__ == '__main__':
    main()
