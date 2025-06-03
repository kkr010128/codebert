import itertools

while True:
	n, x = map(int, input().split()) # n = 5, x = 9

	if (n == 0 and x == 0):
		break

	count = 0
	num_sequence = [i + 1 for i in range(n)] # [1, 2, 3, 4, 5]
	for guess in itertools.combinations(num_sequence, 3):
		sum = 0
		for i in guess:
			sum += i
		if (sum == x):
			# (1, 3, 5)
			# (2, 3, 4)
			count += 1

	print(count)