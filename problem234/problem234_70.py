import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    vec = [[0] * 10 for _ in range(10)]
    for n in range(1, N + 1):
        s = str(n)
        vec[int(s[0])][int(s[-1])] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += vec[i][j] * vec[j][i]

    print(ans)
    return


if __name__ == '__main__':
    main()
