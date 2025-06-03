


N,M = map(int, input().split())
S = input()
cnt = 0
for s in S:
    if s == "0":
        cnt = 0
    else:
        cnt += 1
        if cnt >= M:
            print(-1)
            exit()


"""
辞書順最小
・より少ない回数でゴール
・同じ回数なら、低い数字ほど左にくる

N歩先がゴール　→　出目の合計がNになったらOK
iマス目を踏むとゲームオーバー　→　途中で出目の合計がiになるとアウト

ただ、辞書順が厄介
N=4, 00000があったとして、M=3の場合、3->1より1->3の方が辞書順で若い。なので、スタート地点から貪欲に進めるだけ進む、は条件を満たさない。
→　ゴールからスタートに帰る。移動方法は貪欲にする。
"""

ans = []
rS = S[::-1]
l = 0
r = 1
while l < N:
    r = l + 1
    stoppable = l
    while r - l <= M and r <= N:
        if rS[r] == "0":
            stoppable = r
        r += 1
    
    ans.append(stoppable - l)

    l = stoppable

print(*ans[::-1])