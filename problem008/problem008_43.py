n=int(input())
adj=[]
for i in range(n):
	a=list(map(int,input().split()))
	for j in range(2,len(a)):
		a[j]-=1
	adj.append(a[2:])
visit_time1=[0]*n
visit_time2=[0]*n
visited=[0]*n
def dfs(now):
	global time
	visit_time1[now]=time
	time+=1
	for next in adj[now]:
		if not visited[next]:
			visited[next]=True
			dfs(next)
	visit_time2[now]=time
	time+=1
time=1
for i in range(n):
	if not visited[i]:
		visited[i]=True
		dfs(i)
for i in range(n):
	print(i+1,visit_time1[i],visit_time2[i])
