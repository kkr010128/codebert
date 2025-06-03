if __name__ == '__main__':
	a, b, c = input().split()
	a, b, c = int(a), int(b), int(c)

	if a < b and b < c:
		print("Yes")
	else:
		print("No")
