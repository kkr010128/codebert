while True:
	a,b = list(map(int, input().split()))
	if (a == 0) and (b == 0):
		break
	elif (a < b):
		print(str(a) + " " + str(b))
	else :
		print(str(b) + " " + str(a))