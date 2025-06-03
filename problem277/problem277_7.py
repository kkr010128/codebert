H, W, K = map(int, input().split())

S = [list(input()) for i in range(H)]

C = [-1] * H
for i, r in enumerate(S):
    C[i] = r.count('#')

ans = [[-1] * W for i in range(H)]
first_flg = False
z = []
a = 0
for i in range(H):
    if C[i] == 0:
        if first_flg is False:
            z.append(i)
        else:
            ans[i] = ans[i-1]
    else:
        a += 1
        c = 0
        for j in range(W):
            if S[i][j] == '#':
                first_flg = True
                if c == 0:
                    c += 1
                else:
                    c += 1
                    a += 1
            ans[i][j] = a

for i in z[::-1]:
    ans[i] = ans[i+1]

for i in range(H):
    print(*ans[i])
