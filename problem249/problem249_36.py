import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, K = map(int, readline().split())

    if K < A:
        print(A - K, B)
    elif K < A + B:
        print(0, A + B - K)
    else:
        print(0, 0)

    return


if __name__ == '__main__':
    main()
