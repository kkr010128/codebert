n, m, l = map(int, input().split()) # n = 3, c = 2, l = 3

a_matrix = [list(map(int, input().split())) for row in range(n)] # [[1, 2], [0, 3], [4, 5]]
b_matrix = [list(map(int, input().split())) for row in range(m)] # [[1, 2, 1], [0, 3, 2]]

result_matrix = [[0 for x in range(l)] for y in range(n)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(n):
	for j in range(l):
		for k in range(m):
			result_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]

for i in range(n):
	print(' '.join(map(str, result_matrix[i])))