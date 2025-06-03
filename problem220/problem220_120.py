import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S, T = readline().split()
    A, B = map(int, readline().split())
    U = readline().strip()

    if S == U:
        print(A - 1, B)
    else:
        print(A, B - 1)

    return


if __name__ == '__main__':
    main()
