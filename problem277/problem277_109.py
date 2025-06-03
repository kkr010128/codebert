H,W,K = map(int, input().split())
s = []
for i in range(H):
    s.append(list(input()))

ans = [[0] * W for i in range(H)]
cnt = 0
flg = True
for i in range(H):
    if '#' in s[i]:
        cnt += 1
        sb = 0
        for j in range(W):
            if s[i][j] == '#':
                sb += 1
                if sb > 1:
                    cnt += 1
            ans[i][j] = cnt
            if flg == False:
                for k in range(i):
                    ans[k][j] = cnt
        flg = True
    else:
        if i == 0 or flg == False:
            flg = False
        else:
            for j in range(W):
                ans[i][j] = ans[i-1][j]
    #print(flg)
for i in range(H):
    print(' '.join(map(str,ans[i])))
