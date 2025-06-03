count=int(raw_input())
l=set()
for i in xrange(count):
	a,b=raw_input().split()
	if a=='insert':
		l.add(b)
	elif b in l:
		print 'yes'
	else:
		print 'no'