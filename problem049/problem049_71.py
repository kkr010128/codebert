if __name__ == "__main__":
	lis = []
	while True:
		a, b = map( int, input().split() )
		if a == b == 0:
			break
		lis.append([a,b])
	for i in lis:
		for j in range(i[0]):
			print('#'*i[1])
		print()