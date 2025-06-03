import collections
N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    road[A].append(B)
    road[B].append(A)

no_visit =set(range(1,N+1))
q = collections.deque([])
cnt = 0
while no_visit:
    q.append(no_visit.pop())
    cnt +=1
    while q:
        now = q.popleft()
        for nxt in road[now]:
            if nxt in no_visit:
                q.append(nxt)
                no_visit.discard(nxt)
print(cnt-1)
    
