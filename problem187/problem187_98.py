import itertools

N, X, Y = map(int, input().split())

# 距離が0,1,2,...,n-1のパスの本数
l = [0] * N

# 1,2,...,Nから2つを選ぶ組み合わせ
# 生成される組み合わせ(i,j)は既にi<jになっている
comb = itertools.combinations(range(1, N + 1), 2)

# (直接iとjを繋ぐ)or(特殊なパスを通る)の２種類が考えられる
# 両方計算してminを取れば欲しい距離が得られる
for v in comb:
    min_dist = min(v[1] - v[0], abs(X - v[0]) + 1 + abs(Y - v[1]))
    l[min_dist] += 1

# 距離が1,2,3,...,N-1について総数を出力
for item in l[1:]:
    print(item)
