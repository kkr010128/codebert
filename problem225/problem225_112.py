def serval_vs_monster():
    # 入力
    H, A = map(int, input().split())
    # 処理
    if H % A == 0:
        return H // A
    else:
        return H // A + 1

result = serval_vs_monster()
print(result)