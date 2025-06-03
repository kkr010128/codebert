times, disp_rate = map(int, input().split())

int_rate = 0

# 参加回数が10回未満の場合
if times < 10:
    # 内部レートを計算する
    int_rate = disp_rate + 100 * (10-times)
else:
    int_rate = disp_rate

print(int_rate)