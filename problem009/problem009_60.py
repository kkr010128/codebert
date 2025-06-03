import collections
N = int(input())
P = [[0 for _ in range(N)] for _ in range(N)] 
for i in range(N):
    u,k,*varray = map(int,input().split()) # u,k は数, varray は配列
    for v in varray:
        P[u-1][v-1] = 1    

D = [-1 for _ in range(N)]
D[0] = 0 # 始点への距離は 0, 他の距離は-1
Q = collections.deque()
Q.append(0)
while len(Q) > 0:
    c = Q.popleft()
    for i in range(N):
        if P[c][i]==1 and D[i]==-1:
            D[i] = D[c]+1
            Q.append(i)
for v in range(N):
    print(v+1, D[v])         
