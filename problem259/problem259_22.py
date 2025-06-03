# -*- coding: utf-8 -*-
import sys
from collections import deque

N,u,v=map(int, sys.stdin.readline().split())

al=[ [] for i in range(N+1) ]	#隣接リスト

for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    al[a].append(b)
    al[b].append(a)

dist_t=[ 0 for _ in range(N+1) ] #高橋君のスタート地点からの各頂点までの距離
dist_a=[ 0 for _ in range(N+1) ] #青木君のスタート地点からの各頂点までの距離

#print "al :: ",al

#高橋君のスタート地点からの各頂点までの距離
Visit=[ 0 for _ in range(N+1) ]
q=deque()
q.append(u)
Visit[u]=1

while q:
    fro=q.popleft()
    for to in al[fro]:
        if Visit[to]==0:
            Visit[to]=1 #訪問済みに1をセット
            dist_t[to]=dist_t[fro]+1 #距離を計算
            q.append(to)

#print "dist_t :: ",dist_t

#青木君のスタート地点からの各頂点までの距離
Visit=[ 0 for _ in range(N+1) ]
q=deque()
q.append(v)
Visit[v]=1

while q:
    fro=q.popleft()
    for to in al[fro]:
        if Visit[to]==0:
            Visit[to]=1 #訪問済みに1をセット
            dist_a[to]=dist_a[fro]+1 #距離を計算
            q.append(to)

#print "dist_a :: ",dist_a

ans=0
max_a=0
for t,a in zip(dist_t,dist_a):
    if t<a:
        ans=max(ans,a)

print ans-1