N, K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))
S = []
R = -1000000001
#それぞれについての累積和の計算
for i in range(N):#このループはN個の初期マスの時のループ
    t = i  # tは現在の位置
    cnt = 0  # 累積和
    sum = []  # 累積和のリスト
    res = 0
    while True:#このループは一つの初期マスの累積和。最初のコマに戻るまで
        t = P[t]-1
        cnt += C[t]
        sum.append(cnt)
        if t == i:
            break
    #S.append(sum)
    if len(sum) >=  K:
        res = max(sum[:K])
    else:
        if sum[-1] <= 0:
            res = max(sum)
        else:
            score1 = sum[-1] * (K // len(sum) - 1) + max(sum)
            score2 = sum[-1] * (K // len(sum))
            r = K % len(sum)
            if r != 0:
                score2 += max(0, max(sum[:r]))
            res = max(score1,score2)
    R = max(R,res)
print(R)
