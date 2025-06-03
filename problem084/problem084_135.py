'''
	We can show that if u and v belong to the same connected component, then they are friends w/ each other
	So everyone in a given connected component is friends with one another
	So everyone in a given connected component must be separated into different groups

	If we have a CC of with sz nodes in it, then we need at least sz different groups

	So, the minimum number of groups needed is max sz(CC)
'''
n, m = map(int,input().split())
adj = [[] for u in range(n+1)]
for i in range(m):
	u, v = map(int,input().split())
	adj[u].append(v)
	adj[v].append(u)

vis = [False for u in range(n+1)]
def bfs(s):
	sz = 0
	queue = [s]
	ptr = 0
	
	while ptr < len(queue):
		u = queue[ptr]
		if not vis[u]:
			vis[u] = True
			sz += 1
			for v in adj[u]:
				queue.append(v) 
		ptr += 1

	return sz

CCs = []
for u in range(1,n+1):
	if not vis[u]:
		CCs.append(bfs(u))

print(max(CCs))