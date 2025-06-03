def bingo():
    # 初期処理
    A = list()
    b = list()
    comb_list = list()
    is_bingo = False
    # 入力
    for _ in range(3):
        dummy = list(map(int, input().split()))
        A.append(dummy)
    N = int(input())
    for _ in range(N):
        dummy = int(input())
        b.append(dummy)
    # ビンゴになる組み合わせ
    for i in range(3):
        # 横
        comb_list.append([A[i][0], A[i][1], A[i][2]])
        # 縦
        comb_list.append([A[0][i], A[1][i], A[2][i]])
    # 斜め
    comb_list.append([A[0][0], A[1][1], A[2][2]])
    comb_list.append([A[0][2], A[1][1], A[2][0]])
    # 集計（出現した数字をnullに置き換え)
    for i in b:
        for j in range(8):
            for k in range(3):
                if i == comb_list[j][k]:
                    comb_list[j][k] = 'null'
    # すべてnullのリストの存否
    for i in comb_list:
        for j in i:
            if 'null' != j:
                is_bingo = False
                break
            else:
                is_bingo = True
        # 一組でもbingoがあれば即座に関数を抜ける
        if is_bingo == True:
            return 'Yes'
    # すべてのリストを確認後
    if is_bingo == False:
        return 'No'
        

result = bingo()
print(result)
