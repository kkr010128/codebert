A, B = list(map(int, input().split()))
x = 1
while True:
	a = A * x
	if a % B == 0:
		print(a)
		break
	x += 1