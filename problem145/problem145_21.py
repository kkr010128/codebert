import sys,math,collections,itertools
input = sys.stdin.readline


N,M = list(map(int,input().split()))
road = [[] for _ in range(N+1)]
flag = [-1 for _ in range(N+1)]
flag[1]=0
for i in range(M):
    a,b = map(int,input().split())
    road[a].append(b)
    road[b].append(a)
q = collections.deque([1])
while q:
    now = q.popleft()
    for r in road[now]:
        if flag[r] == -1:
            flag[r] = now
            q.append(r)
            
print('Yes')
for i in range(2,N+1):
    print(flag[i])