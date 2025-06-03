H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

res = float('inf')
for i in range(2**(H-1)):
    c = bin(i).count('1')
    cnt = c
    sum_l = [0] * (c+1)
    j = 0
    flag = True
    while j < W:
        tmp = sum_l.copy()
        pos = 0
        for k in range(H):
            if S[k][j] == '1':
                tmp[pos] += 1
            if (i >> k) & 1:
                pos += 1
        if max(tmp) <= K:
            sum_l = tmp.copy()
            j += 1
            flag = False
        else:
            if flag:
                cnt = float('inf')
                break
            cnt += 1
            flag = True
            sum_l = [0] * (c+1)

    res = min(res, cnt)

print(res)