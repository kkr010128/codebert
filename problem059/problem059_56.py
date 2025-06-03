n, m = map(int, input().split())
li = [list(map(int,input().split())) for i in range(n)]
c = []

for i in range(n):
	li[i].append(sum(li[i]))

for j in range(m+1):
	t = 0
	for i in range(n):
		t += li[i][j]
	c.append(t)
li.append(c)

for i in range(n+1):
	print(*li[i])