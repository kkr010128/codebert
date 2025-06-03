H, W, K = map(int, input().split())

cake = [list(input()) for _ in range(H)]
ans = [[0] * W for _ in range(H)]

id = 1
sign = 0
nothing = 0

for i in range(H):
    if cake[i].count('#') == 0:
        nothing += 1
        if i == H-1:
            for j in range(W):
                for d in range(nothing):
                    ans[i-d][j] = ans[i-nothing][j]
        continue
    for j in range(W):
        if cake[i][j] == '#':
            ans[i][sign:j+1] = [id] * (j+1-sign)
            sign = j+1
            id += 1
        elif j == W-1:
            ans[i][sign:j+1] = [id-1] * (j+1-sign)
    if nothing != 0:
        for j in range(W):
            for d in range(1,nothing+1):
                ans[i-d][j] = ans[i][j]
    sign = 0
    nothing = 0

for i in range(H):
    for j in range(W):
        print('{} '.format(ans[i][j]), end='')
    print()