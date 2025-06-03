# 入出力から得点を計算する
import sys
input = lambda: sys.stdin.readline().rstrip()
D = int(input())
c = list(map(int, input().split()))
s = [[int(i) for i in input().split()] for _ in range(D)]
t = []
for i in range(D):
    tmp = int(input())
    t.append(tmp)

# 得点
result = 0

# 最後に開催された日を保存しておく
last_day = [0 for _ in range(26)]

for i in range(len(t)):
    # 選んだコンテスト
    choose = t[i] - 1

    # 最終開催日を更新
    last_day[choose] = i + 1

    # そのコンテストを選んだ時の本来のポイント
    result += s[i][choose]


    # そこから満足度低下分をマイナス
    for j in range(26):
        result -= c[j] * ((i+1) - last_day[j])
    # result += tmp_point
    print(result)
# print(c,s,t)
