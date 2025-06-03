n = int(input())

l = [0] * 10001

for i in range(1, 101):
	for j in range(1, 101):
		for k in range(1, 101):
			x = i**2 + j**2 + k**2 + i*j + j*k + i*k
			if x <= 10000:
				l[x] += 1

for i in range(1, n+1):
	print(l[i])