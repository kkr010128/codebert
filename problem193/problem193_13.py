import sys
sys.setrecursionlimit(10**9)
INF = 110110110
H, W, K = list(map(int, input().split()))
S = [''] * H
for i in range(H):
    S[i] = input()
ans = H * W

for bit in range(2**(H-1)):
    cnt = bin(bit).count('1')
    id = [0] * H
    for i in range(H-1):
        if bit>>i & 1:
            id[i+1] = id[i] + 1
        else:
            id[i+1] = id[i]
    num = [[0] * W for i in range(id[H-1]+1)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '1':
                num[id[i]][j] += 1
    for i in range(id[H-1]+1):
        for j in range(W):
            if num[i][j] > K:
                cnt = INF
    sum = [0] * (id[H-1]+1)
    for j in range(W):
        need = False
        for i in range(id[H-1]+1):
            if sum[i] + num[i][j] > K:
                need = True
        if need:
            cnt += 1
            for i in range(id[H-1]+1):
                sum[i] = num[i][j]
        else:
            for i in range(id[H-1]+1):
                sum[i] += num[i][j]
    ans = min(ans, cnt)

print(ans)
