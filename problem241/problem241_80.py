#!/usr/bin/env python3
from scipy.sparse.csgraph import csgraph_from_dense, dijkstra
import numpy as np

def main():
    H, W = list(map(int, input().split()))
    N = H * W
    S = [[line for line in range(W)] for row in range(H)]
    for i in range(H):
        row = input()
        for j, line in enumerate(row):
            S[i][j] = line

    data = np.zeros([N, N])
    for i in range(H):
        for j in range(W):
            n = W * i + j
            if j<W-1 and S[i][j]=='.' and S[i][j+1]=='.':
                data[n][n+1] = data[n+1][n] = 1
            if i<H-1 and S[i][j]=='.' and S[i+1][j]=='.':
                data[n][n+W] = data[n+W][n] = 1

    G = csgraph_from_dense(data)
    answer = 0
    for n in range(N):
        result = dijkstra(G, indices=n)
        result = [x for x in result if x!=np.inf]
        answer = max(answer, max(result))
    print(int(answer))
    pass

if __name__ == '__main__':
    main()
