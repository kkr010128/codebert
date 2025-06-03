#coding: UTF-8

l = raw_input().split()

W = int(l[0])
H = int(l[1])
x = int(l[2])
y = int(l[3])
r = int(l[4])

if x >=r:
	if y >=r:
		if x <=(H -r):
			if y <=(H-r):
				print "Yes"
			else:
				print "No"
		else:
			print"No"
	else:
		print "No"

else:
	print "No"