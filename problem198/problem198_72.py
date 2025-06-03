# https://atcoder.jp/contests/panasonic2020/submissions/12881278
# D - String Equivalence
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    def dfs(S, available):
        if len(S) == n:
            print("".join(S))
            return

        for i in range(available + 1):
            S.append(chr(97 + i))
            dfs(S, max(available, i + 1))
            S.pop()

    dfs([], 0)


if __name__ == '__main__':
    resolve()
