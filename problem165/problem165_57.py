def gacha():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]
    # 重複排除
    freebie_tuple = set(S)
    # 景品の種類
    return len(freebie_tuple)

result = gacha()
print(result)