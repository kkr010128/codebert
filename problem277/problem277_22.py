def LI():
    return list(map(int, input().split()))


def LSH(h):
    return [list(input()) for _ in range(h)]


H, W, K = LI()
S = LSH(H)
ans = [[0 for i in range(W)]for j in range(H)]
count = 1
for i in range(H):
    itigo = 0
    ok = 0
    for j in range(W):
        if S[i][j] == "#":
            ok = 1
            if itigo == 0:
                ans[i][j] = count
                itigo = 1
            else:
                count += 1
                ans[i][j] = count

        else:
            ans[i][j] = count
    if ok == 0:
        ans[i][0] = 0
    else:
        count += 1
ok = -1
for i in range(H):
    if ans[i][0] == 0:
        if ok == -1:
            for k in range(i+1, H):
                if ans[k][0] != 0:
                    ok = k
                    break
        for x in range(W):
            print(ans[ok][x], end=" ")
        print()
    else:
        ok = i
        for j in range(W):
            print(ans[i][j], end=" ")
        print()
