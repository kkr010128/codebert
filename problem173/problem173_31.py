# 数字を取得
N = int(input())

# 数値分ループ
calc = []
for cnt in range(1, N + 1):
    # 3もしくは5の倍数であれば、加算しない
    if cnt % 3 != 0 and cnt % 5 != 0:
        calc.append(cnt)

# 合計を出力
print(sum(calc))