import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    ans = 0
    for i in range(N - 2):
        if S[i : i + 3] == 'ABC':
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
