a, b, c = map(int, raw_input().split())

n = a
count = 0

while True:
	x = c % n
	if x == 0:
		count += 1
	
	if n == b:
		break
	else:
		n += 1

print count