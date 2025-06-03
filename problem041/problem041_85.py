l=map(int,raw_input().split())
W=l[0]
H=l[1]
x=l[2]
y=l[3]
r=l[4]
if x>=r and y>=r and x+r<=W and y+r<=H:
	print 'Yes'
else:
	print 'No'