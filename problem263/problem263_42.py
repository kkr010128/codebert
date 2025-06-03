# -*- coding: utf-8 -*-
"""
D - Xor Sum 4
https://atcoder.jp/contests/abc147/tasks/abc147_d

"""
import sys


def solve(N, A):
    MOD = 10**9 + 7
    bit_len = max(map(int.bit_length, A))
    ans = 0
    for i in range(bit_len):
        zeros, ones = 0, 0
        for a in A:
            if (a & 1<<i):
                ones += 1
            else:
                zeros += 1
        ans = (ans + (ones * zeros * 2**i)) % MOD
    return ans % MOD


def main(args):
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
