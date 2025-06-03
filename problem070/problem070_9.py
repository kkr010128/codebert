import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
nextcity = [[] for _ in range(N)]
sgn = [0 for _ in range(N)]
while M:
	M -= 1
	A, B = map(int, input().split())
	A -= 1
	B -= 1
	nextcity[A].append(B)
	nextcity[B].append(A)

def dfs(cnt, city):
	for item in nextcity[city]:
		if sgn[item] == 0:
			sgn[item] = cnt
			dfs(cnt, item)
	return None

cnt = 0
for k in range(N):
	if sgn[k] == 0:
		cnt += 1
		sgn[k] = cnt
		dfs(cnt, k)
print(cnt -1)
