# C問題

# 難しく考えず、入力された配列の先頭の要素から順に見に行く
# cur_maxという、①最大身長格納変数を用意、②①を更新して行く　この2ステップの考え方が大事
N = int(input())
cur_max = 0
ans = 0
# 配列を入力   
A = list(map(int, input().split()))

for i in A:
    if cur_max > i:
        ans += cur_max - i
# どんどん高いものに更新→max関数で処理
    cur_max = max(i, cur_max)
print(ans)