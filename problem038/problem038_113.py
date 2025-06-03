numbers = []
n = raw_input()

numbers = n.split(" ")

for i in range(2):
	numbers[i] = int(numbers[i])

if numbers[0] > numbers[1]:
	print "a > b"
elif numbers[0] < numbers[1]:
	print "a < b"
elif numbers[0] == numbers[1]:
		print "a == b"