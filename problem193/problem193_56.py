H,W,K = map(int, input().split())
S = [input() for _ in range(H)]

L = [[0]*(W) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "1":
            L[i][j] = 1
        
ans = H*W
for i in range(2**(H-1)):
    cnt = 0
    used = [0]*W
    memo = []
    for j in range(H-1):
        if i & (1<<j):
            cnt += 1
            memo.append(j+1)
    memo.append(H)
    num = [0]*(cnt+1)
    for j in range(W):
        idx = 0
        for k in range(H):
            if memo[idx] == k:
                idx += 1
            num[idx] += L[k][j]
        f = False
        for k in range(len(num)):
            if num[k] > K:
                f = True
                break
        if f:
            if j == 0 or used[j-1] == 1:
                cnt = H*W
                break
            used[j-1] = 1
            cnt += 1
            num = [0]*len(num)
            idx = 0
            for k in range(H):
                if memo[idx] == k:
                    idx += 1
                num[idx] += L[k][j]
    ans = min(ans, cnt)
print(ans)