H, W, K = map(int, input().split())
c = []

for _ in range(H):
    c.append(input())
#こういうinputをすると，c_ij = c[i][j] (C[i]という文字列のj文字目)という構造になってくれて，とても嬉しい。
#print(c)

ans = 0

#bit全探索
for rows in range(1 << H):
    #bit演算子。1 << H は二進数で1000...という風に，1の後ろに0がH個並ぶ。
    #例えば rows = 110010 のときには，(2 ** 5ケタ目の1は無視して）（0-indexで）1行目と4行目を赤で塗る状態を指す。
    for cols in range(1 << W):
        black_count = 0

        for i in range(H):
            if (rows >> i) % 2 == 1:continue #i行目が赤で塗られていたならば，何もせずiを一歩進める。

            for j in range(W):
                if (cols >> j) % 2 ==1:continue #j列目が赤で塗られていたならば，何もせずjを一歩進める。
                if c[i][j] == "#":
                    black_count += 1

        if black_count == K:
            ans += 1

print(ans)