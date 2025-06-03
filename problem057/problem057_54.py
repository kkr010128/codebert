import sys

a = sys.stdin.readlines()
for i in range(len(a)):
	b = a[i].split()
	m =int(b[0])
	f =int(b[1])
	r =int(b[2])
	if m*f < 0 :
		print "F"
	elif m==-1 and f==-1 and r==-1:
		break
	else:
		if m+f >= 80:
			print "A"
		elif 80 > m+f >=65:
			print "B"
		elif 65 > m+f >=50:
			print "C"
		elif 50 > m+f >=30 and r < 50:
			print "D"
		elif 50 > m+f >=30 and r >= 50:	
			print "C"
		elif 30 > m+f:
			print "F"