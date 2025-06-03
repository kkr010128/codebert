import sys

readline = sys.stdin.buffer.readline
import math

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    S = readline().decode('utf-8')

    total = S.count('R') * S.count('G') * S.count('B')

    for stride in range(1, math.ceil(N / 2) + 1):
        for start in range(N):
            if start + stride * 2 >= N:
                break
            else:
                if S[start] != S[start + stride] and S[start + stride] != S[start + stride * 2] and S[start + stride * 2] != S[start]:
                    total -= 1

    print(total)


if __name__ == '__main__':
    main()
