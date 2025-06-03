行数, 列数 = map(int, input().split())

#行列の初期化
行列 = [[0 for _ in range(列数)] for __ in range(行数)]

#データをもとに行列を作成
for 現在行 in range(行数):
    行データ = list(map(int, input().split()))
    for 現在列 in range(列数):
        行列[現在行][現在列] = 行データ[現在列]

#ベクトルデータを取得
ベクトル = [0 for _ in range(列数)]
for 現在行 in range(列数):
    ベクトル[現在行] = int(input())

答え = []
#ベクトルを掛ける
for i in range(行数):
    c = 0
    for j in range(列数):
        c += 行列[i][j] * ベクトル[j]
        
    答え.append(c)

#表示
for i in range(len(答え)):
    print(答え[i])
