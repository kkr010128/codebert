from typing import List
from collections import deque

def bfs(G: List[int], s: int) -> None:
	d[s] = 0
	color[s] = "GRAY"
	Q = deque()
	Q.append(s)
	while Q:
		u = Q.popleft()
		for v in G[u]:
			if color[v] == "WHITE":
				color[v] = "GRAY"
				d[v] = d[u] + 1
				pi[v] = u
				Q.append(v)
		color[u] = "BLACK"


if __name__ == "__main__":
	n = int(input())
	G = [[] for _ in range(n)]
	for _ in range(n):
		u, k, *adj = list(map(int, input().split()))
		u -= 1
		G[u] = [v - 1 for v in adj]
	color = ["WHITE" for _ in range(n)]
	d = [-1 for _ in range(n)]
	pi = [None for _ in range(n)]
	bfs(G, 0)
	for i in range(n):
		print(f"{i + 1} {d[i]}")
