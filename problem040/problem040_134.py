numbers = []
n = raw_input()
numbers = n.split(" ")
for i in range(3):
	numbers[i] = int(numbers[i])
flag = 1
while flag:
	flag = 0
	for i in range(2, 0, -1):
		if numbers[i] < numbers[i - 1]:
			numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
			flag = 1
print ' '.join([str(a) for a in numbers])