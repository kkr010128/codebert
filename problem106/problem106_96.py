n = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
	if i*i > n:
		break
	for j in range(1, n + 1):
		z = i*i + j*j + i*j
		if z > n:
			break
		for k in range(1, n + 1):
			
			if (z + k * k + k*i + k * j) > n:
				break
			a[z + k * k + k*i + k * j] += 1
for i in a[1:]:
	print(i)