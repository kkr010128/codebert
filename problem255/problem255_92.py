import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S, T = readline().strip().split()

    ans = []
    for s, t in zip(S, T):
        ans.append(s)
        ans.append(t)

    print(''.join(ans))

    return


if __name__ == '__main__':
    main()
