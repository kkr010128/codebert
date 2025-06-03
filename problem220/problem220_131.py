import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S, T = input().split()
    A, B = map(int, readline().split())
    U = input()

    if S == U:
        A -= 1
    if T == U:
        B -= 1
    print(A, B)


if __name__ == '__main__':
    main()
