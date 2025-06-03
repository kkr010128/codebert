def main():
    # r:ぐー,s:ちょき,p:ぱー
    # 相手のn回目の手についてn%Kの値によってグループ分け
    # 連続して同じ手を出せずに最高点を出す方法を知れば良い
    # 最後に全てを足し合わせる
    N,K = map(int, input().split())
    R,S,P = map(int, input().split())
    T = input()
    hands = [[] for i in range(K)]
    for i in range(N):
        if T[i]=='r': hands[i%K].append(0)
        elif T[i]=='s': hands[i%K].append(1)
        else: hands[i%K].append(2)
    # 貪欲に前から勝てば良い..わけではなさそう
    ans = 0
    points = [R,S,P]
    for i in range(K):
        # dp[j][k] := j回目にkを出した時の最大得点
        dp = [[0]*3 for _ in range(len(hands[i])+1)]
        for j in range(len(hands[i])):
            for k in range(3):
                # kが勝ち手かどうかで場合分け
                if hands[i][j]==(k+1)%3:
                    dp[j+1][k] = max(dp[j+1][k], dp[j][(k+1)%3]+points[k])
                    dp[j+1][k] = max(dp[j+1][k], dp[j][(k+2)%3]+points[k])
                else:
                    dp[j+1][k] = max(dp[j+1][k], dp[j][(k+1)%3])
                    dp[j+1][k] = max(dp[j+1][k], dp[j][(k+2)%3])
        ans += max(dp[-1])
    print(ans)

main()
