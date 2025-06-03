from collections import deque

while True:
	str = input()
	if str == "-":
		break

	dq = deque(char for char in list(str))
	shuffle_count = int(input())

	for i in range(shuffle_count):
		h = int(input())
		dq.rotate(h * -1)

	print(''.join(dq))