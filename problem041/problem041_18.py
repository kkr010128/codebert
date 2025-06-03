W,H,x,y,r=map(int,raw_input().split())
if r<=x<=W-r:
	if r<=y<=H-r:
		print "Yes"
	else:
		print "No"
else:
	print "No"