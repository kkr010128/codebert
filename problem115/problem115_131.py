def calc():
    # 入力
    a = int(input())
    # 計算処理
    result = 0
    for i in range(1,4):
        result += a ** i
    # 出力
    print(result)

calc()