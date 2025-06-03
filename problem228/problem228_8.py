def solve(n):
	if n is 0:
		return 0
	return 1 + 2 * solve(n // 2)

print(solve(int(input())))