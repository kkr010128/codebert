H, W, K = map(lambda x: int(x), input().split())

matrix = []
for i in range(H):
	row = input()
	dots = []
	for j in range(W):
		dots.append(row[j])
	matrix.append(dots)

ans = 0
for bitR in range(1 << H):
	for bitC in range(1 << W):
		black = 0
		for i in range(H):
			for j in range(W):
				if ((bitR >> i) & 1) == 0 and ((bitC >> j) & 1) == 0 and matrix[i][j] == '#':
					black += 1
		if black == K:
			ans += 1

print(ans)



