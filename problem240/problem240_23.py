import sys

input = sys.stdin.readline
_, m = map(int, input().split())

d = {}
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if p in d:  # やっている(やった)問題
        if d[p][0]:  # AC済の問題だった場合
            continue
        if s == "WA":
            d[p][1] += 1
        else:
            d[p][0] = True
    else:  #  初めての問題
        if s == "WA":
            d[p] = [False, 1]  # 中身：AC判定と、ACまでのWAの数
        else:
            d[p] = [True, 0]

cnt_ac = 0
cnt_wa = 0
for v in d.values():
    if v[0]:
        cnt_ac += 1
        cnt_wa += v[1]

print(cnt_ac, cnt_wa)