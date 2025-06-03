a = map(int, raw_input().split())
j = 0
for i in xrange(a[0], a[1]+1):
	j=j if a[2] % i else j+1
print j