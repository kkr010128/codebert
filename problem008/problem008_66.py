from typing import List

def DFS(G: List[int]):
	global time
	time = 0
	n = len(G)
	for u in range(n):
		if color[u] == "WHITE":
			DFS_Visit(u)

def DFS_Visit(u: int):
	global time
	color[u] = "GRAY"
	time += 1
	d[u] = time
	for v in G[u]:
		if color[v] == "WHITE":
			pi[v] = u
			DFS_Visit(v)
	color[u] = "BLACK"
	time += 1
	f[u] = time


if __name__ == "__main__":
	n = int(input())
	G = []
	color = ["WHITE" for _ in range(n)]
	pi = [None for _ in range(n)]
	d = [0 for _ in range(n)]
	f = [0 for _ in range(n)]

	for _ in range(n):
		command = list(map(int, input().split()))
		G.append([x - 1 for x in command[2:]])
	DFS(G)
	for i in range(n):
		print(f"{i + 1} {d[i]} {f[i]}")
