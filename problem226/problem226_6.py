def common_raccoon_vs_monster():
    # 入力
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 必殺技の合計攻撃力
    sum_A = 0 # 必殺技の攻撃力の合計
    for i in range(len(A)):
        sum_A += A[i]
    # 比較
    if H > sum_A:
        return 'No'
    else:
        return 'Yes'

result = common_raccoon_vs_monster()
print(result)