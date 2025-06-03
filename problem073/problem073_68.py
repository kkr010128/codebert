N = int(input())
r = 0
for A in range(1, N+1):
	for B in range(1, N+1):
		if A * B >= N: break
		r += 1
print(r)
