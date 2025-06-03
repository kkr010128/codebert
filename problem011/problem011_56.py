num = map(int, raw_input().split())

if num[0] > num[1]:
	x = num[0]
	y = num[1]
else:
	y = num[0]
	x = num[1]

while y > 0:
	z = x % y
	x = y
	y = z
print x