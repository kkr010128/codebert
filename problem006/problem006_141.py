# Debt Hell

n = int(input())

value = 100000

for i in xrange(n):
	value *= 1.05
	if value % 1000 != 0:
		value = int(value / 1000 + 1) * 1000

print value