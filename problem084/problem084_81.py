'''
	We can show that if u and v belong to the same connected component, then they are friends w/ each other
	So everyone in a given connected component is friends with one another
	So everyone in a given connected component must be separated into different groups

	If we have a CC of with sz nodes in it, then we need at least sz different groups

	So, the minimum number of groups needed is max sz(CC)
'''
import sys
sys.setrecursionlimit(2*10**5+5)

n, m = map(int,input().split())
adj = [[] for u in range(n+1)]
for i in range(m):
	u, v = map(int,input().split())
	adj[u].append(v)
	adj[v].append(u)

vis = [False for u in range(n+1)]
def dfs(u):
	if vis[u]:
		return 0
	vis[u] = True

	sz = 1
	for v in adj[u]:
		sz += dfs(v)
	return sz

CCs = []
for u in range(1,n+1):
	if not vis[u]:
		CCs.append(dfs(u))

print(max(CCs))