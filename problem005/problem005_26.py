def GCD_cal(a,b):
	if(b==0):
		return(a)
	a,b=b,a%b
	return(GCD_cal(a,b))

while(True):
	try:
		a,b=map(int,input().split(" "))
	except:
		break
	if(a<b):
		a,b=b,a
	GCD=GCD_cal(a,b)
	LCM=int(a*b/GCD)
	print("{0} {1}".format(GCD,LCM))