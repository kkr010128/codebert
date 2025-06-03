from copy import deepcopy
from sys import stdin
input = stdin.readline
H,W,K = map(int, input().split())
mat = [list(input()) for _ in range(H)]
ans = 0
for b_i in range(2**H):
    mat_1 = deepcopy(mat)
    for i in range(H):
        if b_i >> i & 1:
            for col in range(W):
                mat_1[i][col] = '.'
        
    for b_j in range(2**W):
        mat_2 = deepcopy(mat_1)
        for j in range(W):
            if b_j >> j & 1:
                for row in range(H):
                    mat_2[row][j] = '.'

        cnt = 0
        for row in mat_2:
            cnt += row.count('#')
        if cnt == K:
            ans += 1
print(ans)