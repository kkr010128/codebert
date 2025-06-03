n = int(raw_input())

print "",

for i in xrange(3,n+1):
	x = i
	if x % 3 == 0:
		print i,
		continue
	while x:
		if x % 10 == 3:
			print i,
			break

		elif x / 10 != 0:
			x = x / 10
			continue
		else:
			break