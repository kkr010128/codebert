# ゴール：3.5.15の倍数 以外の数字を合計したい
N = int(input())

sum_exclusion = 0  # 計算結果を入れる変数

for i in range(1, N + 1):
    if not (i % 15 == 0 or i % 3 == 0 or i % 5 == 0):
        sum_exclusion += i  # rangeが空になるまで、条件に合う数値が足されていく

print(sum_exclusion)
