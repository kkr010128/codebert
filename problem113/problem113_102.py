import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

from numba import njit


def getInputs():
    D = int(readline())
    CS = np.array(read().split(), np.int32)
    C = CS[:26]
    S = CS[26:].reshape((-1, 26))
    return D, C, S


@njit('(i8, i4[:], i4[:, :], i4[:], )', cache=True)
def _compute_score1(D, C, S, out):
    score = 0
    last = np.zeros((D, 26), np.int32)
    for d in range(len(out)):
        if d:
            last[d, :] = last[d - 1, :]
        i = out[d]
        score += S[d, i]
        last[d, i] = d + 1
        score -= np.sum(C * (d + 1 - last[d, :]))
    return last, score


def _update_score():
    pass

@njit('(i8, i4[:], i4[:, :], i4[:], i8, )', cache=True)
def _random_update(D, C, S, out, score):
    d = np.random.randint(0, D)
    q = np.random.randint(0, 26)
    p = out[d]
    out[d] = q

    if p == q:
        return out, score

    last, new_score = _compute_score1(D, C, S, out)
    if score < new_score:
        score = new_score
    else:
        out[d] = p

    return out, score


def _random_swap():
    pass


def step1(D, C, S):
    out = []
    LAST = 0
    for d in range(D):
        max_score = -10000000
        best_i = 0
        
        for i in range(26):
            out.append(i)
            last, score = _compute_score1(D, C, S, np.array(out, np.int32))
            if max_score < score:
                max_score = score
                LAST = last
                best_i = i
            out.pop()

        out.append(best_i)

    return np.array(out), LAST, max_score


def step2(D, C, S, out, score):
    for i in range(10 ** 4):
        out = out.astype(np.int32)
        out, score = _random_update(D, C, S, out, score)
    return out, score


def output(out):
    out += 1
    print('\n'.join(out.astype(str).tolist()))


D, C, S = getInputs()
out, _, score = step1(D, C, S)
#print(score)
out, score = step2(D, C, S, out, score)
output(out)
#print(score)