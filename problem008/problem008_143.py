from sys import stdin

X = [ 0 for i in range(100) ]
d = [ 0 for i in range(100) ]
f = [ 0 for i in range(100) ]
G = [[ 0 for i in range(100) ] for i in range(100)]

t = 0

def DFS(i) :
	global t
	t += 1
	d[i] = t
	for j in range(n) :
		if G[i][j] != 0 and d[j] == 0 : DFS(j)
	t += 1
	f[i] = t


n = int(input())
for i in range(n) :
	X[i] = stdin.readline().strip().split()


for i in range(n) :
	for j in range(int(X[i][1])) :
		G[int(X[i][0])-1][int(X[i][j+2])-1] = 1

for i in range(n) :
	if d[i] == 0 : DFS(i)

for i in range(n) : print(i+1,d[i],f[i])