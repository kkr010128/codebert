N = int(input())
A = list(map(int, input().split()))

if N == 0 and A[0] != 1:                            # N=0なら葉は1
    ans = -1
elif N != 0 and A[0] != 0:                          # N>0ならd=0の葉は0
    ans = -1
else:
    ans = 1                                         # 頂点合計
    node = 1                                        # 深さdの頂点
    lateFolia = sum(A)                              # 残りの葉
    preFolia = 0                                    # 深さd-1の葉

    for d in range(1, N+1):                         # d=0は初期値固定なのでd=1以降の計算
        folia = A[d]                                # 深さdの葉
        node = min((node-preFolia)*2, lateFolia)    # 深さdの頂点の上界 (以下の条件を満たすもの)
                                                    # ・深さd-1の頂点のうち葉ではないものの個数の2倍
                                                    # ・残りの葉の数 (*深さdも含む)

        if node < folia:                            # 頂点<葉はありえない
            ans = -1
            break

        ans += node                                 # 頂点合計を更新
        lateFolia -= folia                          # 残りの葉の数を更新
        preFolia = folia                            # 深さd-1の葉を記憶

print(ans)
