count = input()

for i in range(count):
	l = map(int, raw_input().split())
	l.sort()
	if(l[2]**2==l[0]**2+l[1]**2):
		print "YES"
	else:
		print "NO"