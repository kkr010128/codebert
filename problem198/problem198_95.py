import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    def dfs(s, num):
        if len(s) == n:
            print(s)
            return

        for i in range(num + 1):
            t = s + chr(97 + i)
            dfs(t, max(num, i + 1))

    dfs("", 0)


if __name__ == '__main__':
    resolve()
