import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    ans = 0

    for a in range(1, N):
        for b in range(1, N):
            x = a * b
            if x >= N:
                break
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
