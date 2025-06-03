# 数値の取得
holi,hw = map(int,input().split())
hw_day = list(map(int,input().split()))

# 判定結果を出力
hw_sum = sum(hw_day)
if hw_sum <= holi:
    print(holi - hw_sum)
else:
    print("-1")