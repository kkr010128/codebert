def black_jack():
    # 入力
    A1, A2, A3 = map(int, input().split())
    # 初期処理
    sum = A1 + A2 + A3
    # 判別処理
    if sum >= 22:
        return 'bust'
    elif sum <= 21:
        return 'win'

result = black_jack()
print(result)