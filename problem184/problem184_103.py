def similar_coffee():
    # 入力
    S = input()
    # 判別処理
    if S[2] == S[3] and S[4] == S[5]:
        return 'Yes'
    else:
        return 'No'

result = similar_coffee()
print(result)