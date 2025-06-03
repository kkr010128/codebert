H, W = map(int, input().split())
arr = [input().rstrip() for h in range(H)]
ans = [[0] * W for _ in range(H)]
for h, row in enumerate(arr):
    for w, val in enumerate(row):
        if h == 0 and w == 0:
            if arr[h][w] == "#":
                ans[h][w] = 1
            continue
        nv = 1e+9
        if h > 0:
            nv = ans[h-1][w]
            if arr[h-1][w] == "." and val == "#":
                nv += 1
        if w > 0:
            tmp = ans[h][w-1]
            if arr[h][w-1] == "." and val == "#":
                tmp += 1
            nv = min(nv, tmp)
        ans[h][w] = nv
print(ans[-1][-1])
