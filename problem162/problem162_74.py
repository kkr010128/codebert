N, M = map(int, input().split())
for i in range((M + 1) // 2):
	print(i + 1, i + (M - 2 * i) + 1)
for i in range(M - (M + 1) // 2):
	print(M + 1 + i + 1, M + 1 + i + (M - 1 - 2 * i) + 1)