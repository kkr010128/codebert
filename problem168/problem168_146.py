# 高橋君の夏休みが N 日間
# 夏休みの宿題が M個出されており、i 番目の宿題をやるには　A i日間かかる
# 条件　複数の宿題を同じ日にはできない。
# また宿題をやる日は遊べない。
# 夏休み中に全ての宿題を終わらせるとき、最大何日遊ぶことができるか。
# 終わらない時は-1

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 宿題にかかる合計日数
play_day = N - sum(A)

if play_day < 0:
    print("-1")
else:
    print(play_day)