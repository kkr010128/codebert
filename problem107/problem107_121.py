N = int(input())
X = str(input())
F = [0] * N

def calc_f(n:int)->int:
    global F
    x = n
    res = 0
    while 0 < x:
        if F[x] != 0:
            res += F[x]
            break
        pop = bin(n).count('1')
        x %= pop
        res += 1
    F[n] = res

# 前処理 N以下のF値テーブル
for i in range(1, N):
    calc_f(i)

# ビット反転すると初期の1の個数に対して+1または-1どちらか
pop_ini = X.count('1')
pp = pop_ini + 1  # pop_plus
pm = pop_ini - 1  # pop_minus

# 2進の各桁をppとpmで割った値のテーブル
ap = [0] * N  # arr_plus
am = [0] * N  # arr_minus
for i in range(N):
    ap[i] = pow(2, N-1-i, pp)
    if 0 < pm:
        am[i] = pow(2, N-1-i, pm)

# 所与のXで計算、ベースになる値
fp = 0  # f_plus
fm = 0  # f_minus
for i in range(N):
    if X[i] == '1':
        fp = (fp + ap[i]) % pp
        if 0 < pm:
            fm = (fm + am[i]) % pm

# 各桁を反転した場合では差分更新のみ
for i in range(N):
    ans = 1
    if X[i] == '1':
        if 0 < pm:
            v = (fm + pm - am[i]) % pm
        else:
            ans = 0
            v = 0
    else:
        v = (fp + ap[i]) % pp
    if 0 < v:
        ans += F[v]
    print(ans)