import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, readline().split())
    if A < 10 and B < 10:
        print(A * B)
    else:
        print(-1)

    return


if __name__ == '__main__':
    main()
