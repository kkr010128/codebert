# 各行の所属するグループを配列として持たせる実装。列ごと見ていってダメなら垂直線追加していく
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ans = 10**9
for bit in range((1 << (H-1))):
    vidx = []
    gok = True
    g = 0
    gid = [0] * H
    for i in range(H-1):
        if (bit >> i) & 1:
            g += 1
        gid[i+1] = g
    g += 1
    gnum = [0]*g
    vertical = 0
    for w in range(W):
        ok = True
        one = [0]*g
        for h in range(H):
            one[gid[h]] += int(S[h][w])
            gnum[gid[h]] += int(S[h][w])
            if one[gid[h]] > K:
                gok = False
            if gnum[gid[h]] > K:
                ok = False
        if not ok:
            vertical += 1
            vidx.append(w)
            gnum = one

    # if bit == 2:
    #    print('aaaaa')
    #    print(gid)
    #    print(vidx)
    #    print(bin(bit), g-1, vertical)
    #    print('aaaaa')
    if gok:
        if ans > g-1 + vertical:
            ans = g-1 + vertical
            # print(bin(bit), g-1, vertical)
            # print(vidx)
            # print(ans)
        # ans = min(ans, g-1 + vertical)
if ans == 10**9:
    print(-1)
else:
    print(ans)
