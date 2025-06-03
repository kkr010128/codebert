import queue
N=int(input())
M=[input().split()[2:]for _ in[0]*N]
q=queue.Queue();q.put(0)
d=[-1]*N;d[0]=0
while q.qsize()>0:
 u=q.get()
 for v in M[u]:
  v=int(v)-1
  if d[v]<0:d[v]=d[u]+1;q.put(v)
for i in range(N):print(i+1,d[i])
