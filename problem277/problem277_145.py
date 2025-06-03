H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = [[0] * W for _ in range(H)]

def calc(h, w, k):
    #上下方向の限界を決める
    up = h
    for i in range(1, h + 1):
        if S[h - i][w] == '.' and ans[h - i][w] == 0:
            if h == i:
                up = 0
            continue
        else:
            up = h - (i - 1)
            break

    down = h
    for i in range(1, H - h):
        if S[h + i][w] == '.' and ans[h + i][w] == 0:
            if i == H - h - 1:
                down = H - 1
            continue
        else:
            down = h + (i - 1)
            break
    # print ('up, down =', up, down, i)
    # up から down までの縦の長さの長方形を作る。
    for i in range(up, down + 1):
        ans[i][w] = k
    
    flag = True
    for i in range(1, w + 1):
        for j in range(up, down + 1):
            if ans[j][w - i] == 0 and S[j][w - i] == '.':
                continue
            else:
                flag = False
                break
        if not flag:
            break
        for j in range(up, down + 1):
            ans[j][w - i] = k
    flag = True
    for i in range(1, W - w):
        for j in range(up, down + 1):
            if ans[j][w + i] == 0 and S[j][w + i] == '.':
                continue
            else:
                flag = False
                break
        if not flag:
            break
        for j in range(up, down + 1):
            ans[j][w + i] = k
        


k = 1
for w in range(W):
    for h in range(H):
        if S[h][w] == '#':
            # print (h, w)
            calc(h, w, k)
            k += 1

for tmp in ans:
    print (*tmp, sep = ' ')