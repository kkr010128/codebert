"""
Hが少ないので、縦で割るパターンは全探索して見る。
dpとか使わずに、貪欲的に割っていけばよい。

"""
H,W,K = map(int,input().split())
choco = [list(input()) for _ in range(H)]
accum = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        accum[i][j] = accum[i][j-1] + int(choco[i][j])

ans = float("INF")
for i in range(2**H):
    """
    i を2進数表記したときに1になっているインデックスに該当する行数で分割する。
    例えば00100なら3行目と4行目の間で分割する。
    """
    binI = format(i,"0"+str(H)+"b")
    group = {}
    groupNum = 0
    for j in range(H):
        group[j] = groupNum
        if binI[j] == "1":
            groupNum += 1
    breakCnt = groupNum
    tmp = [0]*(groupNum+1)
    for j in range(W):
        tmp2 = [0]*(groupNum+1)
        for k in range(H):
            groupNum = group[k]
            if choco[k][j] == "1":
                tmp2[groupNum] += 1
        if max(tmp2) > K:
            break
        else:
            for l in range(groupNum+1):
                tmp[l] += tmp2[l]
            if max(tmp) > K:
                breakCnt += 1
                tmp = tmp2
    else:
        ans = min(ans,breakCnt)
print(ans)