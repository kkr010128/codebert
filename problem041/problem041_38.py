a=raw_input()
list=a.split()
W=int(list[0])
H=int(list[1])
x=int(list[2])
y=int(list[3])
r=int(list[4])
if r<=x<=W-r and r<=y<=H-r:
	print 'Yes'
else:
	print 'No'