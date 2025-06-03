def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)

import sys
import numpy as np
from math import gcd
mod = 10**9+7
def pow_mod(base, exp):  # [pow_mod, "i8(i8,i8)"],
    # mod はグローバル変数を参照
    exp %= mod - 1
    res = 1
    while exp:
        if exp % 2:
            res = res * base % mod
        base = base * base % mod
        exp //= 2
    return res

def solve(N, AB):
    n = 0
    na = nb = nab = 0
    Cnt = {}
    for a, b in zip(AB[::2], AB[1::2]):
        if (a, b) == (0, 0):
            nab += 1
        elif a == 0:
            na += 1
        elif b == 0:
            nb += 1
        else:
            if b < 0:
                a, b = -a, -b
            g = gcd(a, b)
            a //= g
            b //= g
            ab_fr = (a, b)
            n += 1
            if ab_fr in Cnt:
                Cnt[ab_fr] += 1
            else:
                Cnt[ab_fr] = 1
            inv = (-b, a) if a > 0 else (b, -a)
            if inv not in Cnt:
                Cnt[inv] = 0
    ans = (pow_mod(2, na) + pow_mod(2, nb) - 1) % mod
    A = []
    for ab_fr, cnt in Cnt.items():
        a, b = ab_fr
        inv = (-b, a) if a > 0 else (b, -a)
        cnt2 = Cnt[inv]
        p = pow_mod(2, cnt)
        p2 = pow_mod(2, cnt2)
        A.append((p + p2 - 1) % mod)
    A.sort()
    for a in A[::2]:
        ans = ans * a % mod
    ans += nab - 1
    return ans % mod

numba_compile([
    [pow_mod, "i8(i8,i8)"],
    [solve, "i8(i8,i8[:])"],
])

def main():
    N = int(sys.stdin.buffer.readline())
    m = np.array(sys.stdin.buffer.read().split(), dtype=np.int64)
    ans = solve(N, m)
    print(ans)

main()
