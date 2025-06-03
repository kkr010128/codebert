# -*- coding: utf-8 -*-

def input_int_array():
    return map(int, input().split())


MOD = 998244353


def answer():
    n, k = input_int_array()
    spans = [tuple(input_int_array()) for x in range(k)]

    count = [0] * (n)
    count[0] = 1
    accum = [0] * (n + 1)
    accum[1] = 1

    for i in range(1, n):
        j = i + 1
        for l, r in spans:
            start = max(0, j - r - 1)
            end = max(0, j - l)
            count[i] += accum[end] - accum[start]
        accum[j] = accum[j-1] + count[i] % MOD
    print(count[n-1] % MOD)


answer()
