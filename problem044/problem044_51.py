a, b, c = map(int, raw_input().split())
counter = 0
for i in xrange(a, b+1):
	if c % i == 0:
		counter += 1

print counter