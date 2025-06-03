def main():
    # 区間スケジューリングの典型問題
    # 選べる中で最小の終点を選んでいく
    N = int(input())
    sec = [[0,0] for _ in range(N)]
    for i in range(N):
        X,L = map(int, input().split())
        sec[i][0] = X+L
        sec[i][1] = X-L
    # 終点で昇順ソート
    sec = sorted(sec)
    ans = 1
    now = sec[0][0]
    for i in range(1,N):
        if sec[i][1]>=now:
            # 残す
            ans += 1
            now = sec[i][0]
    print(ans)

main()
