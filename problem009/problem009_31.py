#木ではない
#非連結成分
#処理済みの判定、辺の距離はすべて1なので一度到達すればよい
from collections import deque

n = int(input())
V = [[] for _ in range(n+1)]
for _ in range(n):
    inpt = list(map(int,input().split( )))
    if len(inpt)>2:
        V[inpt[0]] = inpt[2:]

lrg = 10000
D = [lrg]*(n+1)
End = [0]*(n+1)

D[1] = 0
Deq = deque()

time = 1
Q = [1]
Deq.append(1)

while len(Deq) > 0:
    v = Deq.popleft()
    for i in V[v]:
        D[i] = min(D[i],D[v]+1)
        if End[i] == 0:
            Deq.append(i)
        End[i] = 1


for i in range(1,n+1):
    if D[i]<lrg-1:
        print(i,D[i])
    else:
        print(i,-1)

