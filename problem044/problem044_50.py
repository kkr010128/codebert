val = map(int,raw_input().split())
count = 0
for x in xrange(val[0], val[1] + 1):
	pass
	if val[2] % x == 0:
		count+=1
print count