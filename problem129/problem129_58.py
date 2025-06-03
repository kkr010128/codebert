# 問題文誤読して30分経過してた
# ソートしたとき「自分より小さいいずれの値も自分の素因数に含まれない」
# これはなんか実装しにくいので、A<10^6を利用して、調和級数的なノリでやってみる
n = int(input())
a = sorted(list(map(int, input().split())))

t = {}
for av in a:
    if av not in t:
        t[av] = 1
    else:
        t[av] += 1
limit = a[-1]

d = [True] * (limit + 1)
for av in a:
    start = av
    # 複数あった場合は自分自身も粛清の対象になる
    if t[av] == 1:
        start *= 2
    for i in range(start, limit + 1, av):
        d[i] = False

ans = 0
for av in a:
    if d[av]:
        ans += 1

print(ans)