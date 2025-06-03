if __name__ == '__main__':

	n,m = map(int,input().split())
	
	a = n // m
	b = n % m
	if b == 0:
		print(a)
	else:
		if a == 0:
			print("1")
		else:
			print(a+1)
