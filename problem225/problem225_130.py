import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, A = map(int, read().split())

    print((H + A - 1) // A)

    return


if __name__ == '__main__':
    main()
