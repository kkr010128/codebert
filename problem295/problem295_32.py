from scipy.sparse.csgraph import csgraph_from_dense
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np
N,M,L=map(int,input().split())
A=[0]*M
B=[0]*M
C=[0]*M
for i in range(M):
    A[i],B[i],C[i] = map(int,input().split())
    A[i] -=1
    B[i] -=1
Q=int(input())
ST=[list(map(int,input().split())) for _ in range(Q)]


G = csr_matrix((C, (A, B)), shape=(N, N))
d = floyd_warshall(G, directed=False)
G=np.full((N,N), np.inf)
G[d<=L]=1
G = csr_matrix(G)
E = floyd_warshall(G, directed=False)

for s,t in ST:
    if E[s-1][t-1]==float('inf'):
        print(-1)
    else:
        print(int(E[s-1][t-1]-1))