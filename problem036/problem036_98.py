a = raw_input()
for i, b in enumerate(a.split()):
	if i==0:
		x=int(b)
	else:
		y=int(b)
print x*y,x*2+y*2