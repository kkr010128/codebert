i = 1
n = int(input())
while i <= n:
	x = i
	if x % 3 == 0:
		print('' , i , end = '')
	else:
		while x:
	 		if x % 10 == 3:
	 			print('' , i , end = '')
	 			break
	 		x = int(x / 10)
	i = i + 1
print('')