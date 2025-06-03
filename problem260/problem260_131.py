import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A = list(map(int, readline().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")


if __name__ == '__main__':
    main()
