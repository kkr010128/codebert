a = map(int, raw_input().split())
while a != [0,0]:
	print '#' * a[1]
	for i in xrange(a[0]-2):
		print '#' + '.' * (a[1] - 2) + '#'
	print '#' * a[1]
	a = map(int, raw_input().split())
	print ""