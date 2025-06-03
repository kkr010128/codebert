"""
高橋君はとりあえず、青木君から最も遠い木の端を目指すのがベスト。
また、目指すべき木の端までの距離に関しては、高橋くんよりも自分の方が近くなくてはならない。
また、高橋君が捕まるときは、必ず木の端の一歩手前のノードになる。
つまり、青木君が移動しなくてはいけない最大距離は、高橋君が目指す木の端までの距離-1、ということになる。
とりま、高橋くん、青木君の初期位置から各ノードまでの距離を調べて、上記の条件にマッチする端を見つける。
"""
from collections import deque
N,u,v = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

takahashi = [None]*(N+1)
que = deque([(0,u,0)])
while que:
    step,cur,par = que.popleft()
    takahashi[cur] = step
    for nx in edges[cur]:
        if nx == par:
            continue
        que.append((step+1,nx,cur))

aoki = [None]*(N+1)
que = deque([(0,v,0)])
while que:
    step,cur,par = que.popleft()
    aoki[cur] = step
    for nx in edges[cur]:
        if nx == par:
            continue
        que.append((step+1,nx,cur))
ans = 0
for i in range(1,N+1):
    if takahashi[i] < aoki[i]:
        ans = max(ans,aoki[i]-1)
print(ans)