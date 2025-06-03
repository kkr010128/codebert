n, k = map(int, input().split())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
negs = [-x for x in A if x < 0]
non_negs = [x for x in A if x >= 0]


def inv(a):
    return pow(a, mod - 2, mod)


# 負の数を選ばざるを得ない数を考える
# 選べる負の数の個数の最小
n_min = k - (max(n - len(negs), 0))
# 　選べる負の数の個数の最大
n_max = min(n, k)

# この2数が一致していて、更に奇数のときにのみ負になる。(はず)
if n_max == n_min and n_max % 2 == 1:
    negs.sort()
    non_negs.sort()
    cnt = 0
    ans = 1
    n_idx, nn_idx = 0, 0
    while cnt < k:
        if n_idx == len(negs):
            ans *= non_negs[nn_idx]
            nn_idx += 1
        elif nn_idx == len(non_negs):
            ans *= -negs[n_idx]
            n_idx += 1
        else:
            if non_negs[nn_idx] < negs[n_idx]:
                ans *= non_negs[nn_idx]
                nn_idx += 1
            else:
                ans *= -negs[n_idx]
                n_idx += 1
        ans %= mod
        cnt += 1

    print(ans % mod)
    exit()

negs.sort(reverse=True)
non_negs.sort(reverse=True)

cnt = 0
ans = 1
neg_cnt = 0
n_idx, nn_idx = 0, 0
# idx番号と配列の長さを比較して、その配列から取得可能かをみる
while cnt < k:
    if n_idx == len(negs):
        ans *= non_negs[nn_idx]
        nn_idx += 1
    elif nn_idx == len(non_negs):
        ans *= -negs[n_idx]
        n_idx += 1
        neg_cnt += 1
    else:
        if non_negs[nn_idx] > negs[n_idx]:
            ans *= non_negs[nn_idx]
            nn_idx += 1
        else:
            ans *= -negs[n_idx]
            n_idx += 1
            neg_cnt += 1
    ans %= mod
    cnt += 1

# 動かす余地がない場合→negが偶数個or動かす余裕がない
if neg_cnt % 2 == 0 or n == k:
    # REからここがおかしそう…
    print(ans % mod)
    exit()
else:
    # 次にかけるのはnegs[n_idx] or non_negs[nn_idx]
    # 一つ戻すならnegs[n_idx-1] or non_negs[nn_idx-1]

    # negsが右にずらせるかどうか
    if n_idx == len(negs) or nn_idx == 0:
        ans *= inv(-negs[n_idx - 1])
        ans *= non_negs[nn_idx]
        ans %= mod
    # non_negsが右にずらせるか
    elif nn_idx == len(non_negs) or n_idx == 0:
        ans *= inv(non_negs[nn_idx - 1])
        ans *= -negs[n_idx]
        ans %= mod
    else:
        # 両方ともずらせないのはすでに除外済み(のはず)
        if non_negs[nn_idx] * non_negs[nn_idx - 1] > negs[n_idx] * negs[n_idx - 1]:
            ans *= non_negs[nn_idx]
            ans *= inv(-negs[n_idx - 1])
            ans %= mod
        else:
            ans *= -negs[n_idx]
            ans *= inv(non_negs[nn_idx - 1])
            ans %= mod

    print(ans % mod)
    exit()
