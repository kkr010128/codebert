import copy
import random
import time


def down(d, last, c):
    result = 0
    for i in range(26):
        result += c[i] * (d - last[i])
    return result


def calc_score_of_the_day(S, d, t, last, C):
    return S[d][t] - down(d+1, last, C) + C[t] * (d+1 - last[t])


def main():
    start = time.time()
    D = int(input())
    C = [int(c) for c in input().split()]

    S = [0] * D

    for d in range(D):
        S[d] = [int(s) for s in input().split()]

    last = [0] * 26
    scores = [float('-inf')] * D

    result = 0
    T = [0] * D
    for d in range(D):
        next_t = 0
        score = float('-inf')
        for t in range(26):
            s = calc_score_of_the_day(S, d, t, last, C)
            if s > score:
                score = s
                next_t = t
        last[next_t] = d + 1
        result += score
        scores[d] = result
        T[d] = next_t + 1


    while time.time() - start < 1.9:
        result = scores[-1]
        change_date = 4 #random.randint(0, D-1)
        change_from = T[change_date]
        change_to = 13 # random.randint(1, 26)

        if change_from == change_to:
            continue
        copied_T = copy.copy(T)
        copied_T[change_date] = change_to

        last_of_the_day = [t if t < change_date else 0 for t in last]
        copied_scores = copy.copy(scores)
        for d in range(change_date, D):
            t = copied_T[d] - 1
            score = calc_score_of_the_day(S, d, t, last_of_the_day, C)
            last_of_the_day[t] = d + 1
            before = copied_scores[d-1] if d > 0 else 0
            copied_scores[d] = before + score
            copied_T[d] = t + 1
        if copied_scores[-1] > result:
            scores = copied_scores
            T = copied_T



    for t in T:
        print(t)


if __name__ == "__main__":
    main()
