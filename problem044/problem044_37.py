# Python 3
if __name__ == "__main__":
	a, b, c = input().split()
	a, b, c = int(a), int(b), int(c)
	count = 0
	for i in range(a, b + 1):
		if c % i == 0:
			count += 1
	print(count)