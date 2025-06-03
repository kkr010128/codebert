x = 1
while x != '0':
	x = input()
	if x != '0':
		sum = 0
		for s in x:
			sum += int(s)
		print(sum)