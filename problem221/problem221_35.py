def i_miss_you():
    # 入力
    S = input()
    # 初期処理
    string = ''
    # 処理
    for _ in range(len(S)):
        string += 'x'
    return string

result = i_miss_you()
print(result)