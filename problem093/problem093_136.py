INF = float("inf")

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = -INF
for s in range(N):
    ### STEP1
    cum = []
    i = P[s] - 1 #s-> i
    cum.append(C[i])
    while i != s:
        i = P[i] - 1
        cum.append(cum[-1] + C[i])
    

    # STEP2
    if K <= len(cum):
        #1週未満しかできない
        score = max(cum[:K])
    
    elif cum[-1] <= 0:
        #一周以上できるが、ループしたら損する場合
        score = max(cum)
    else:
        # K//Length - 1回だけループし、最後は最適に止まる
        score1 = cum[-1] * (K//len(cum) - 1)
        score1 += max(cum)

        #ループをK//length回だけループする場合
        score2 = cum[-1]*(K//len(cum))
        resi = K % len(cum) #残り進める回数
        if resi != 0:
            #まだ進めるなら
            score2 += max(0, max(cum[:resi]))
        score = max(score1, score2)
    
    ans = max(ans, score)

print(ans)
