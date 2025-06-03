import copy
import random
import sys
import time
from collections import deque

t1 = time.time()

readline = sys.stdin.buffer.readline


global NN
NN = 26


def evaluate(D, C, S, out, k):
    score = 0
    last = [0 for _ in range(NN)]

    for d in range(len(out)):
        last[out[d]] = d + 1
        for i in range(NN):
            score -= (d + 1 - last[i]) * C[i]

        score += S[d][out[d]]

    for d in range(len(out), min(D, len(out) + k)):
        for i in range(NN):
            score -= (d + 1 - last[i]) * C[i]

    return score


def compute_score(D, C, S, out):
    score = 0
    last = [0 for _ in range(NN)]

    for d in range(len(out)):
        p = out[d]
        last[p] = d + 1
        last[out[d]] = d + 1
        for i in range(NN):
            score -= (d + 1 - last[i]) * C[i]

        score += S[d][out[d]]

    return score


def solve(D, C, S, k):
    out = deque()
    for _ in range(D):
        max_score = -10 ** 8
        best_i = 0

        for i in range(NN):
            out.append(i)
            score = evaluate(D, C, S, out, k)
            if max_score < score:
                max_score = score
                best_i = i
            out.pop()
        out.append(best_i)

    return out, score


# 1箇所ランダムに変える
def random_change(D, C, S, out, score):
    new_out = copy.deepcopy(out)
    d = random.randrange(0, D)
    new_out[d] = random.randrange(0, NN)
    new_score = compute_score(D, C, S, new_out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


def random_change0(D, C, S, out, score):
    new_out = copy.deepcopy(out)
    d = random.randrange(0, 10)
    new_out[d] = random.randrange(0, NN)
    new_score = compute_score(D, C, S, new_out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


# N箇所ランダムに変える
def random_changeN(D, C, S, out, score, N):
    new_out = copy.deepcopy(out)
    for _ in range(N):
        d = random.randrange(0, D)
        new_out[d] = random.randrange(0, NN)

    new_score = compute_score(D, C, S, new_out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


# 2つswap
def random_swap2(D, C, S, out, score):
    d1 = random.randrange(0, D - 1)
    d2 = random.randrange(d1 + 1, min(d1 + 16, D))
    new_out = copy.deepcopy(out)
    new_out[d1], new_out[d2] = out[d2], out[d1]
    new_score = compute_score(D, C, S, out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


# ３つswap
def random_swap3(D, C, S, out, score):
    d1 = random.randrange(0, D - 1)
    d2 = random.randrange(d1 + 1, min(d1 + 8, D))
    d3 = random.randrange(max(d1 - 8, 0), d1 + 1)
    new_out = copy.deepcopy(out)
    new_out[d1], new_out[d2], new_out[d3] = out[d2], out[d3], out[d1]
    new_score = compute_score(D, C, S, out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


def random_swap0(D, C, S, out, score):
    d1 = random.randrange(0, 6)
    d2 = random.randrange(6, 13)
    new_out = copy.deepcopy(out)
    new_out[d1], new_out[d2] = out[d2], out[d1]
    new_score = compute_score(D, C, S, out)

    if new_score > score:
        score = new_score
        out = new_out

    return out, score


def main():
    D = int(readline())
    C = list(map(int, readline().split()))
    S = [list(map(int, readline().split())) for _ in range(D)]

    # ランダムな初期値
    # out = [random.randrange(0, NN) for _ in range(D)]

    # 貪欲法で初期値を決める
    max_score = -10 ** 8
    max_k = 0

    for k in range(6):
        out, score = solve(D, C, S, k)

        if score > max_score:
            max_score = score
            max_out = out
            max_k = k

    # # local minimumを避けるため,outを少し変える
    out = max_out
    score = max_score

    out, score = solve(D, C, S, max_k)

    out[0] = random.randrange(NN)

    for cnt in range(10 ** 10):
        out, score = random_changeN(D, C, S, out, score, N=1)
        out, score = random_swap3(D, C, S, out, score)

        t2 = time.time()
        if t2 - t1 > 1.85:
            break

    ans = [str(i + 1) for i in out]
    print("\n".join(ans))


main()
