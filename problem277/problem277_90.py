
def resolve():
    H, W, K = map(int, input().split())
    G = [list(input()) for _ in range(H)]

    ans = [[0] * W for _ in range(H)]
    cnt, first = 1, -1
    for i in range(H):
        tmp = 0
        if "#" in G[i]:
            if first == -1:
                first = i
            for j in range(W):
                if G[i][j] == "#":
                    tmp += 1
                    if tmp > 1:
                        cnt += 1
                ans[i][j] = cnt
            cnt += 1
        else:
            if i > 0:
                ans[i] = ans[i - 1][:]

    for q in range(first):
        ans[q] = ans[first][:]

    for i in range(H):
        print(*ans[i])


if __name__ == "__main__":
    resolve()
