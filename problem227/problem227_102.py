if __name__ == '__main__':

	n,k = map(int,input().split())
	A = list(map(int,input().split()))
	
	A.sort()

	num = len(A) - min(n,k)

	print(sum(A[0:num]))
