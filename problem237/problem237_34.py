def resolve():
    """
    典型的な区間スケジューリング問題
    各スケジュールの終了時間が短いものから選択していけば，
    選択するスケジュール数が最大になる．
    今回は腕の可動範囲上限の小さいものから選択していく．
    """
    import sys
    
    readline = sys.stdin.readline

    N = int(readline())
    XL = [list(map(int, readline().split())) for _ in [0] * N]

    # 腕の可動範囲の(上限, 下限)のリスト生成
    t = [(x + length, x - length) for x, length in XL]
    
    # 複数要素を含む要素のsortではインデックスの小さい要素から比較していきソート
    t.sort()               # リストを腕の上限の昇順(小さい順)でソート
    time = -float('inf')   # time=0でもおｋ
    ans = 0
    for i in range(N):
        end, start = t[i]  # tはソート済故，上限が小さい順に選出される
        if time <= start:  # 腕の下限が既存の腕と重ならないか判定
            ans += 1
            time = end     # 現在の腕の上限を記録
    print(ans)

if __name__ == "__main__":
    resolve()
