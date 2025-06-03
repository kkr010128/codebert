N, M, K = map(int, input().split())
chess = [input() for i in range(N)]
ans = [[0 for i in range(M)] for j in range(N)]
index = 0


def ok(r, h, t):
    for i in range(h, t+1):
        if ans[r][i] or chess[r][i] == '#':
            return False
    return True


def color(r, h, t):
    for i in range(h, t+1):
        ans[r][i] = index


# mother fucker
for i in range(N):
    j = 0
    while j < M:
        if chess[i][j] == '.':
            j += 1
            continue
        index += 1
        l = j - 1
        while l >= 0 and chess[i][l] == '.' and ans[i][l] == 0:
            l -= 1
        l += 1
        r = j + 1
        while r < M and chess[i][r] == '.' and ans[i][r] == 0:
            r += 1
        r -= 1
        # [l,r]
        # color
        color(i, l, r)
        for k in range(i-1, -1, -1):
            if ok(k, l, r):
                color(k, l, r)
            else:
                break
        for k in range(i+1, N):
            if ok(k, l, r):
                color(k, l, r)
            else:
                break
        j = r + 1

for i in range(N):
    for j in range(M-1):
        print(ans[i][j], end='')
        print(' ', end='')
    print(ans[i][M-1], end='')
    print("")
