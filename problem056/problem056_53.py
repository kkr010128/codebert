n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for j in range(m)]

for a_row in a:
	print(sum(a_row[k] * b[k] for k in range(m)))