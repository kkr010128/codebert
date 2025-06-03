n = int(raw_input())
d = [100 for i in range(n)]
G = [0 for i in range(n)]
v = [[0 for i in range(n)] for j in range(n)]

def BFS(s):
	for e in range(n):
		if v[s][e] == 1:
			if d[e] > d[s] + 1:
				d[e] = d[s]+1
				BFS(e)

for i in range(n):
	G = map(int, raw_input().split())
	for j in range(G[1]):
		v[G[0]-1][G[j+2]-1] = 1
d[0] = 0

for i in range(n):
	BFS(i)
for i in range(n):
	if d[i] == 100:
		d[i] = -1
for i in range(n):
	print i+1, d[i]