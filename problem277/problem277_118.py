import sys

H, W, K = map(int, input().split())
S = [list(sys.stdin.readline().strip()) for _ in range(H)]

i = 0
j = 0
ichigo = False
no = False
for i in range(H):
    j = 0
    if len(set(S[i])) == 1 and "." in S[i]:
        no = True
        continue
    while j < W:
        if S[i][j] == ".":
            S[i][j] = str(K)
        else:
            if ichigo is True:
                j -= 1
                K -= 1
                ichigo = False
            else:
                S[i][j] = str(K)
                ichigo = True
        j += 1
    ichigo = False
    K -= 1

if no is True:
    for i in range(H):
        if S[i][0] != ".":
            tmp = i
    for i in reversed(range(tmp)):
        if S[i][0] == ".":
            for j in range(W):
                S[i][j] = S[i + 1][j]
    for i in range(tmp + 1, H):
        if S[i][0] == ".":
            for j in range(W):
                S[i][j] = S[i - 1][j]
for i in range(H):
    print(*S[i])
