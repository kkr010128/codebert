import sys
input()
d = set()
for l in sys.stdin:
	c,s = l.split()
	if c[0] == 'i':
		d.add(s)
	else:
		print('yes' if s in d else 'no')
