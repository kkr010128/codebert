
n = input()
s = []
h = []
c = []
d = []
for i in range(n):
	spare = raw_input().split()
	if spare[0]=='S':
		s.append(int(spare[1]))
	elif spare[0]=='H':
		h.append(int(spare[1]))
	elif spare[0]=='C':
		c.append(int(spare[1]))
	else :
		d.append(int(spare[1]))
for j in range(1,14):
	judge = True
	for k in range(len(s)):
		if j==s[k] :
			judge = False
			break
	if judge :
		print 'S %d' %j
for j in range(1,14):
	judge = True
	for k in range(len(h)):
		if j==h[k] :
			judge = False
			break
	if judge :
		print 'H %d' %j
for j in range(1,14):
	judge = True
	for k in range(len(c)):
		if j==c[k] :
			judge = False
			break
	if judge :
		print 'C %d' %j
for j in range(1,14):
	judge = True
	for k in range(len(d)):
		if j==d[k] :
			judge = False
			break
	if judge :
		print 'D %d' %j