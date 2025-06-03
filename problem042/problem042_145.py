import sys
c = 0
while True:
	x = int(sys.stdin.readline())
	if x == 0:
		break
	c+=1
	print ('Case ' + str(c)+':', x)