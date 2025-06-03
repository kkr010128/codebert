D = int(input())
C = list(map(int,input().split()))
S = [list(map(int,input().split())) for _ in range(D)]

# B
T = [int(input()) for _ in range(D)]

# 初期化
ans = 0 # 満足度
last = [-1]*26

# 満足度を計算
for d in range(D):
    # 開催するコンテストID
    contest_id = T[d]-1
    # 満足度をプラス
    ans += S[d][contest_id]
    # 最終開催日を更新
    last[contest_id] = d
    # 開催されなかったコンテストの処理
    for i in range(26):
        ans -= C[i]*(d - last[i])
    # 出力
    print(ans)
