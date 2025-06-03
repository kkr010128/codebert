import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    ans = []

    def dfs(s):

        if len(s) == N:
            ans.append(s)
            return

        maxs = max(map(ord, s))
        for i in range(ord('a'), maxs + 2):
            dfs(s + chr(i))

    dfs('a')
    print('\n'.join(sorted(ans)))


if __name__ == '__main__':
    main()
