from random import randint
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
    last = [0]*26  # コンテストiを前回開催した日
    for d in range(ct):
        last[T[d]] = d + 1
    prei = T[ct]  # 変更前に開催する予定だったコンテストi
    score -= S[ct][prei]
    score += S[ct][ci]
    for d in range(ct, D):
        if d != ct and T[d] == prei:
            break
        score += C[prei]*(d + 1 - ct - 1)
        score -= C[prei]*(d + 1 - last[prei])
    for d in range(ct, D):
        if d != ct and T[d] == ci:
            break
        score += C[ci]*(d + 1 - last[ci])
        score -= C[ci]*(d + 1 - ct - 1)
    T[ct] = ci
    return score, T


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
    for k in range(5, 10):
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
    ct = randint(0, D-1)
    ci = randint(0, 25)
    for _ in range(400000):
        new_score, new_T = update_score(D, C, S, T, score, ct, ci)
        if score < new_score:
            score = new_score
            T = new_T
    return T


if __name__ == '__main__':
    D = int(input())
    C = [int(i) for i in input().split()]
    S = [[int(i) for i in input().split()] for j in range(D)]
    init_score, T = greedy(D, C, S)
    T = local_search(D, C, S, init_score, T)
    for t in T:
        print(t+1)
