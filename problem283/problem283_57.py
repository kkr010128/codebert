N = int(input())
ctr = 0
if N <= 2:
	print(0)
else:
	if (N - 2) % 2 == 0:
		print(N // 2 - 1)
	else:
		print((N - 1) // 2)
