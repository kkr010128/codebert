def solve(a):
	for i in range(1, 10):
		if a % i == 0 and 1 <= a // i <= 9:
			return "Yes"
	return "No"
print(solve(int(input())))