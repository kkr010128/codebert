N = int(input())
cnt = 0
for A in range(1, N + 1):
	for B in range(1, N // A + 1):
		C = N - A * B
		if C >= 1 and A * B + C == N:
			cnt += 1
print(cnt)
