import sys
while True:
	x,y = map(int,input().split())
	if (x==0) and (y==0):
		break
	for i in range(0,x):
		for j in range(0,y):
			sys.stdout.write("#")	
		sys.stdout.write("\n")
	sys.stdout.write("\n")