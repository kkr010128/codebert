N,X,Y = map(int,input().split())

from collections import deque

INF = 1000000000
ans = [0]*(N-1)


def rep(sv,dist):
    que = deque()

    def push(v,d):
        if (dist[v] != INF): return
        dist[v] = d
        que.append(v)

    push(sv,0)

    while(que):
        v = que.popleft()
        d = dist[v]

        if v-1 >= 0:
            push(v-1, d+1)
        if v+1 < N:
            push(v+1, d+1)
        if v == X-1:
            push(Y-1, d+1)
        #逆に気を付ける
        if v == Y-1:
            push(X-1, d+1)

for i in range(N):
    dist = [INF]*N
    rep(i,dist)
    # print(dist)
    for d in dist:
        if d-1 == -1:continue
        ans[d-1] += 1


for an in ans:
    print(an//2)
# print(ans)






