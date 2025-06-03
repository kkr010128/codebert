small = []
large = []

while True:
	input_a, input_b = map(int, raw_input().split())
	if input_a == 0 and input_b == 0:
		break
	else:
		if input_a < input_b:
			small.append(input_a)
			large.append(input_b)
		else:
			small.append(input_b)
			large.append(input_a)

for (n, m) in zip(small, large):
		print n, m