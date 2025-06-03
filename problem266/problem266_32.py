x=int(input())
 
if x<100:
	print("0")
	exit()

while 1:
	tm=(str(x)[-2:])
	if int(tm) > 5:
		x-=105
	else:
		print("1")
		exit()
		
	if x<100:
		print("0")
		exit()
