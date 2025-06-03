import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    counter = Counter(S)
    ans = counter['R'] * counter['G'] * counter['B']

    for i in range(N):
        for j in range(i + 1, (N + i + 1) // 2):
            if 2 * j - i >= N:
                break
            if S[i] != S[j] and S[i] != S[2 * j - i] and S[j] != S[2 * j - i]:
                ans -= 1

    print(ans)
    return


if __name__ == '__main__':
    main()
