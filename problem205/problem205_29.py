from collections import defaultdict

N, P = map(int, input().split())
S = input()

"""
S = "s0 s1 ... s(N-1)"に対して"sl s(l+1) ... s(r-1)"が素数Pで割り切れるかを考える。
これはa_i := int("si s(i+1) ... s(N-1)")と定めることで、
    (a_l - a_r) / 10^{N-r} ¥cong 0  (mod P)
と定式化できる。

（整数関連の区間の問題は後ろからの累積和が相性良さそう。頭からの累積を考えたのが敗因な気がする）

Pが2でも5でもない場合は、上式は
    a_l - a_r ¥cong 0 (mod P)
に同値であるから、各a_iのmod Pでの値を辞書にまとめておけば良さそう。
Pが2, 5のいずれかの場合は偶然チェックが簡単なので解ける。
"""

ans = 0
if P == 2:
    for i in range(N):
        a = int(S[i])
        if a % 2 == 0:
            ans += i + 1
elif P == 5:
    for i in range(N):
        a = int(S[i])
        if a == 0 or a == 5:
            ans += i + 1
else:
    S += "0" # 上の定式化の都合上、r = Nのケースが必要なので
    d = defaultdict(int)
    r = 0
    d[0] += 1
    for i in range(N - 1, -1, -1):
        """
        ここでS[i:]を毎回Pで割るとTLEする（桁の大きい演算はやはり負担が大きいのか？）
        (a_i % P)をi = N, N-1,...の降順に求めていくことを考えれば、
        前の計算結果が使える、特に繰り返し二乗法が使えるのでだいぶ早くなるみたい。
        """
        r += int(S[i]) * pow(10, N - i - 1, P)
        r %= P
        d[r] += 1

    for num in d.values():
        ans += num * (num - 1) // 2

print(ans)
