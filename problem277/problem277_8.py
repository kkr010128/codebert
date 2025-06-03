H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]
cur = 1
for i in range(H):
    has_st = []
    for j in range(W):
        if S[i][j] == "#":
            has_st.append(j)
    if not has_st:
        continue
    elif len(has_st) == 1:
        ans[i] = [cur] * W
        cur += 1
    else:
        for j in range(has_st[-1] + 1):
            ans[i][j] = cur
            if S[i][j] == "#":
                cur += 1
        ans[i][has_st[-1] + 1 :] = [cur - 1] * (W - has_st[-1] - 1)

for i in range(H - 1):
    if ans[i + 1] == [0] * W:
        ans[i + 1] = ans[i][:]
for i in range(H - 1, 0, -1):
    if ans[i - 1] == [0] * W:
        ans[i - 1] = ans[i][:]
[print(" ".join(map(str, row))) for row in ans]
