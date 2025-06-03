H, W, K = map(int, input().split())
S = [list(map(int, input())) for _ in range(H)]

ans = 100000
for i in range(2**H):
    cnt = 0
    temp = i
    group = [0]*H
    for j in range(H):
        group[j] = cnt
        if temp & 1:
            cnt += 1
        temp >>= 1
    div = [0]*H
    for j in range(W):
        for k in range(H):
            if div[group[k]] + S[k][j] > K:
                cnt += 1
                div = [0]*H
                for l in range(H):
                    div[group[l]] += S[l][j]
                    if div[group[l]] > K:
                        cnt = 100000
                break
            else:
                div[group[k]] += S[k][j]
    ans = min(ans, cnt)
print(ans)
    
