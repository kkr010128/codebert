N = int(input())

count = 0
for i in range(1, N):
	if i != N - i:
		count += 1
print(count // 2)
