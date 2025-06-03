
def resolve():
    R, C, K = map(int, input().split())
    G = [[0] * (C+1) for _ in range(R+1)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        G[r][c] = v

    DP1 = [0 for _ in range(C + 1)]  # c列目までとったとき、最新の行で1個以下とったという条件のもとの最大
    DP2 = [0 for _ in range(C + 1)]  # c列目までとったとき、最新の行で2個以下とったという条件のもとの最大
    DP3 = [0 for _ in range(C + 1)]  # c列目までとったとき、最新の行で3個以下とったという条件のもとの最大

    for r in range(1, R+1):
        for c in range(1, C+1):
            # 更新の順番に注意
            # mid = max(DP1[c], DP2[c], DP3[c]) + I[r][c]
            mid = DP3[c] + G[r][c]
            DP3[c] = max(DP3[c - 1], mid, DP2[c - 1] + G[r][c])  # 3個
            DP2[c] = max(DP2[c - 1], mid, DP1[c - 1] + G[r][c])  # 2個
            DP1[c] = max(DP1[c - 1], mid)  # 1個

    print(DP3[C])

if __name__ == "__main__":
    resolve()