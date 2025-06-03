N, K = map(int, input().split())

data = list(map(int, input().split()))

for x in range(K):
#	print(data)
	raise_data = [0] * (N + 1)
	for i, d in enumerate(data):
		raise_data[max(0, i - d)] += 1
		raise_data[min(N, i + d + 1)] -= 1
	
	height = 0
	ended = 0
	for i in range(N):
		height += raise_data[i]
		data[i] = height
		if height == N:
			ended += 1
	
	if ended == N:
#		print(x)
		break
	
print(*data)
