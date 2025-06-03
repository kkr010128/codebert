if __name__ == '__main__':

	h,n = map(int,input().split())
	A = list(map(int,input().split()))
	sm = sum(A)
	if h <= sm:
		print("Yes")
	else:
		print("No")
