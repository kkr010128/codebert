def numtoalpha(n):
	
	if n <= 26:
		return chr(96+n)
	elif n % 26 == 0:
		return numtoalpha(n//26-1) + chr(96+26)
	else :
		return numtoalpha(n//26) + chr(96+(n%26))

if __name__ == '__main__':

	n = int(input())

	print(numtoalpha(n))
