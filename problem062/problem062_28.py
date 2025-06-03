while True :
	x = input()
	if x==0:
		break
	else:
		Count = 0
		while x>0 :
			Count += x%10
			x /= 10
		print '%d' %Count