# A - 9x9
# 九九の計算
# 九九以外は -1 を返す

# 整数 a b を入力
a, b = map(int, input().split())

# print(a, b)

# a b が9以下の数字か判定し結果を代入
if a <= 9:
    if b <= 9:
        answer = a * b
    else:
        answer = -1
else:
    answer = -1

# 結果の表示
print(answer)
