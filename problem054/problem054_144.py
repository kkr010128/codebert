s = range(1,14)
h = range(1,14)
c = range(1,14)
d = range(1,14)

n = input()

for i in range(n):
	mark, number = raw_input().split()

	if mark == 'S':
		s[int(number)-1] = 0
	elif mark == 'H':
		h[int(number)-1] = 0
	elif mark == 'C':
		c[int(number)-1] = 0
	elif mark == 'D':
		d[int(number)-1] = 0

for i in range(13):
	if s[i] != 0:
		print "S %d" %s[i]
for i in range(13):
	if h[i] != 0:
		print "H %d" %h[i]
for i in range(13):
	if c[i] != 0:
		print "C %d" %c[i]
for i in range(13):
	if d[i] != 0:
		print "D %d" %d[i]