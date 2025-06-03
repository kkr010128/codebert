import math
a = raw_input()
for i, b in enumerate(a.split()):
	if i==0:
		W=int(b)
	elif i==1:
		H=int(b)
	elif i==2:
		x=int(b)
	elif i==3:
		y=int(b)
	else:
		r=int(b)
if r<=x<=W-r and r<=y<=H-r:
	print 'Yes'
else:
	print 'No'