import math

ans = []
while True:
	data = input().split()
	a = int(data[0])
	b = data[1]
	c = int(data[2])

	if b == '+':
		ans += [a+c]
	elif b == '-':
		ans += [a-c]
	elif b == '*':
		ans += [a*c]
	elif b == '/':
		ans += [math.floor(a/c)]
	elif b == '?':
		break
	else:
		break

for output in ans:
	print(output)
