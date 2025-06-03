def ABC_swap():
    # 入力
    X, Y, Z = map(int, input().split())
    A = X
    B = Y
    C = Z
    # 入れ替え処理
    A, B = B, A
    A, C = C, A
    # 表示
    print(A, B, C)

ABC_swap()