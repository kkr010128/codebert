import sys

import numpy as np
from numba import njit


@njit('(i8[:],)', cache=True)
def solve(inp):
    def bitree_sum(bit, t, i):
        s = 0
        while i > 0:
            s += bit[t, i]
            i ^= i & -i
        return s

    def bitree_add(bit, n, t, i, x):
        while i <= n:
            bit[t, i] += x
            i += i & -i

    def bitree_lower_bound(bit, n, d, t, x):
        sum_ = 0
        pos = 0
        for i in range(d, -1, -1):
            k = pos + (1 << i)
            if k <= n and sum_ + bit[t, k] < x:
                sum_ += bit[t, k]
                pos += 1 << i
        return pos + 1

    def initial_score(d, ccc, sss):
        bit_n = d + 3
        bit = np.zeros((26, bit_n), dtype=np.int64)
        INF = 10 ** 18
        for t in range(26):
            bitree_add(bit, bit_n, t, bit_n - 1, INF)

        ttt = np.zeros(d, dtype=np.int64)
        last = np.full(26, -1, dtype=np.int64)
        score = 0

        for i in range(d):
            best_t = 0
            best_diff = -INF
            costs = ccc * (i - last)
            costs_sum = costs.sum()

            for t in range(26):
                tmp_diff = sss[i, t] - costs_sum + costs[t]
                if best_diff < tmp_diff:
                    best_t = t
                    best_diff = tmp_diff
            ttt[i] = best_t
            last[best_t] = i
            score += best_diff
            bitree_add(bit, bit_n, best_t, i + 2, 1)

        return bit, score, ttt

    def calculate_score(d, ccc, sss, ttt):
        last = np.full(26, -1, dtype=np.int64)
        score = 0

        for i in range(d):
            t = ttt[i]
            last[t] = i
            score += sss[i, t] - (ccc * (i - last)).sum()

        return score

    def update_score(bit, bit_n, bit_d, ccc, sss, ttt, d, q):
        diff = 0
        t = ttt[d]
        k = bitree_sum(bit, t, d + 2)
        c = bitree_lower_bound(bit, bit_n, bit_d, t, k - 1) - 2
        e = bitree_lower_bound(bit, bit_n, bit_d, t, k + 1) - 2
        b = ccc[t]
        diff -= b * (d - c) * (e - d)
        diff -= sss[d, t]

        k = bitree_sum(bit, q, d + 2)
        c = bitree_lower_bound(bit, bit_n, bit_d, q, k) - 2
        e = bitree_lower_bound(bit, bit_n, bit_d, q, k + 1) - 2
        b = ccc[q]
        diff += b * (d - c) * (e - d)
        diff += sss[d, q]

        return diff

    d = inp[0]
    ccc = inp[1:27]
    sss = np.zeros((d, 26), dtype=np.int64)
    for r in range(d):
        sss[r] = inp[27 + r * 26:27 + (r + 1) * 26]

    bit, score, ttt = initial_score(d, ccc, sss)
    bit_n = d + 3
    bit_d = int(np.log2(bit_n))
    loop = 6 * 10 ** 6
    tolerant_min = -3000.0
    best_score = score
    best_ttt = ttt.copy()

    for lp in range(loop):
        cd = np.random.randint(0, d)
        ct = np.random.randint(0, 26)
        while ttt[cd] == ct:
            ct = np.random.randint(0, 26)

        diff = update_score(bit, bit_n, bit_d, ccc, sss, ttt, cd, ct)

        progress = lp / loop

        if diff > (1 - progress) * tolerant_min:
            score += diff
            bitree_add(bit, bit_n, ttt[cd], cd + 2, -1)
            bitree_add(bit, bit_n, ct, cd + 2, 1)
            ttt[cd] = ct

        if score > best_score:
            best_score = score
            best_ttt = ttt.copy()

    return best_ttt + 1


inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print('\n'.join(map(str, ans)))
