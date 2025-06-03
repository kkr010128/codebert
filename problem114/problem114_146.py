def data_input():
    D = int(input())
    C = tuple(map(int, input().split()))

    S = []
    for i in range(D):
        s = tuple(map(int, input().split()))
        S.append(s)

    return D, C, S


def score(D, C, S, T):
    """入力D, C, Sと出力Tからスコアを計算する関数"""

    last = [0] * 26  # 0で初期化されている

    def decrease(d, last):
        """d日めにiを開催した時の満足度の減少を返す関数"""
        res = 0
        for i in range(26):
            ith = C[i] * (d+1 - last[i])
            res -= ith
        return res

    V = []  # V[d]はd日めの満足度を表す
    for d, i in enumerate(T):
        if d == 0:
            v = 0
        last[i] = d + 1
        v += S[d][i] + decrease(d, last)
        V.append(v)
    return V

D, C, S = data_input()

T = []
for i in range(D):
    t = int(input()) - 1
    T.append(t)

V = score(D, C, S, T)

for v in V:
    print(v)