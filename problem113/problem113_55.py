from random import randint, random
from math import exp
import sys
input = sys.stdin.readline
INF = 9223372036854775808


def calc_score(D, C, S, T):
    """
    開催日程Tを受け取ってそこまでのスコアを返す
    コンテストi 0-indexed
    d 0-indexed
    """
    score = 0
    last = [0]*26  # コンテストiを前回開催した日
    for d, t in enumerate(T):
        last[t] = d + 1
        for i in range(26):
            score -= (d + 1 - last[i]) * C[i]
        score += S[d][t]
    return score


def update_score(D, C, S, T, score, ct, ci):
    """
    ct日目のコンテストをコンテストciに変更する
    スコアを差分更新する

    ct: change t 変更日 0-indexed
    ci: change i 変更コンテスト 0-indexed
    """
    new_score = score
    last = [0]*26  # コンテストiを前回開催した日
    prei = T[ct]  # 変更前に開催する予定だったコンテストi
    for d, t in enumerate(T, start=1):
        last[t] = d
        new_score += (d - last[prei])*C[prei]
        new_score += (d - last[ci])*C[ci]
    last = [0]*26
    for d, t in enumerate(T, start=1):
        if d-1 == ct:
            last[ci] = d
        else:
            last[t] = d
        new_score -= (d - last[prei])*C[prei]
        new_score -= (d - last[ci])*C[ci]
    new_score -= S[ct][prei]
    new_score += S[ct][ci]
    return new_score


def evaluate(D, C, S, T, k):
    """
    d日目終了時点での満足度を計算し，
    d + k日目終了時点での満足度の減少も考慮する
    """
    score = 0
    last = [0]*26
    for d, t in enumerate(T):
        last[t] = d + 1
        for i in range(26):
            score -= (d + 1 - last[i]) * C[i]
        score += S[d][t]

    for d in range(len(T), min(len(T) + k, D)):
        for i in range(26):
            score -= (d + 1 - last[i]) * C[i]
    return score


def greedy(D, C, S):
    Ts = []
    for k in range(7, 10):
        T = []  # 0-indexed
        max_score = -INF
        for d in range(D):
            # d+k日目終了時点で満足度が一番高くなるようなコンテストiを開催する
            max_score = -INF
            best_i = 0
            for i in range(26):
                T.append(i)
                score = evaluate(D, C, S, T, k)
                if max_score < score:
                    max_score = score
                    best_i = i
                T.pop()
            T.append(best_i)
        Ts.append((max_score, T))
    return max(Ts, key=lambda pair: pair[0])


def local_search(D, C, S, score, T):
    T0 = 2e3
    T1 = 6e2
    Temp = T0
    for k in range(500, 95000):
        if k % 100:
            t = (k/95000) / 1.9
            Temp = pow(T0, 1-t) * pow(T1, t)
        sel = randint(1, 2)
        if sel == 1:
            # ct 日目のコンテストをciに変更
            ct = randint(0, D-1)
            ci = randint(0, 25)
            new_score = update_score(D, C, S, T, score, ct, ci)
            lim = random()
            if score < new_score or \
                    (new_score > 0 and exp((score - new_score)/Temp) > lim):
                T[ct] = ci
                score = new_score
        else:
            # ct1 日目と ct2 日目のコンテストをswap
            ct1 = randint(0, D-1)
            ct2 = randint(0, D-1)
            ci1 = T[ct1]
            ci2 = T[ct2]
            new_score = update_score(D, C, S, T, score, ct1, ci2)
            new_score = update_score(D, C, S, T, new_score, ct2, ci1)
            lim = random()
            if score < \
                    (new_score > 0 and exp((score - new_score)/Temp) > lim):
                score = new_score
                T[ct1] = ci2
                T[ct2] = ci1
    return T


if __name__ == '__main__':
    D = int(input())
    C = [int(i) for i in input().split()]
    S = [[int(i) for i in input().split()] for j in range(D)]
    init_score, T = greedy(D, C, S)
    T = local_search(D, C, S, init_score, T)
    for t in T:
        print(t+1)
