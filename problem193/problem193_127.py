H, W, K = map(int, input().split())
S = [list(map(int, list(input()))) for _ in range(H)]

ans = H*W

def countWhite(ytop, ybottom, xleft, xright):
    ret = sum([sum(s[xleft:xright]) for s in S[ytop:ybottom]])
    return ret
    

for h_div in range(1 << H-1):
    count = 0
    cut = [0]
    for i in range(H):
        if h_div >> i & 1:
            cut.append(i+1)
            count += 1
    cut.append(H)
    if count > ans:
        continue
    
    left = 0
    # ここどんなふうに縦に切っても条件を満たさない場合がある
    for right in range(1, W+1):
        white = 0
        for i in range(len(cut)-1):
            white = max(white, countWhite(cut[i], cut[i+1], left, right))
        
        if white > K:
            if left == right - 1: # 条件を満たす縦の切り方がなかった場合
                break
            left = right - 1
            count += 1
            if count > ans:
                break
    else:
        if count < ans:
            ans = count

print(ans)